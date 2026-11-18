"""Real loopback room-note lifecycle and refusal tests; synthetic local scope only."""
from concurrent.futures import ThreadPoolExecutor
import http.client
import inspect
import json
from pathlib import Path
import socket
import tempfile
import threading
import unittest
from unittest.mock import patch

from muse_presets.personal_companion import CompanionScope, PersonalCompanion
from muse_presets.room_notebook import RoomNotebook
from muse_presets.space_server import make_server

ROOT = Path(__file__).resolve().parents[1]


class RoomHttpTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="companion-room-http-")
        self.db = Path(self.tmp.name).resolve() / "notes.sqlite3"
        self.scope = CompanionScope("owner", "space", "owner", True)
        self.token = "local-test-session-" + "x" * 32
        self.server = None
        self.start()
        self.addCleanup(self.cleanup)

    def start(self, enabled=True):
        # On the old source this starts its existing server and yields a real
        # 404 RED, rather than an unrelated unexpected-keyword exception.
        options = {"companion_home": enabled} if "companion_home" in inspect.signature(make_server).parameters else {}
        self.server = make_server(self.db, token=self.token, authority=lambda: self.scope, **options)
        self.thread = threading.Thread(target=self.server.serve_forever,
                                       kwargs={"poll_interval": 0.01})
        self.thread.start()
        self.port = self.server.server_address[1]
        self.origin = "http://127.0.0.1:" + str(self.port)

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.thread.join(5)
            self.assertFalse(self.thread.is_alive())
            self.server = None

    def cleanup(self):
        self.stop()
        self.tmp.cleanup()

    def call(self, path, body=None, *, method="POST", headers=None, auth=True):
        h = {"Authorization": "Bearer " + self.token} if auth else {}
        if body is not None:
            h["Content-Type"] = "application/json"
        h.update(headers or {})
        payload = json.dumps(body) if isinstance(body, dict) else body
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        try:
            connection.request(method, path, payload, h)
            result = connection.getresponse()
            return result.status, dict(result.getheaders()), result.read()
        finally:
            connection.close()

    def put(self, room="notebook", ident="note1", text="One thought", revision=0):
        return self.call("/api/room/put", {"room_id": room, "note_id": ident,
                         "text": text, "expected_revision": revision})

    def listing(self, room="notebook"):
        status, _, raw = self.call("/api/room/list", {"room_id": room})
        self.assertEqual(status, 200, raw)
        return json.loads(raw)

    def test_create_read_update_delete_and_room_isolation(self):
        status, _, raw = self.put()
        self.assertEqual(status, 200, raw)
        self.assertEqual(json.loads(raw)["revision"], 1)
        self.assertEqual(self.put("garden", text="Water on Friday")[0], 200)
        self.assertEqual(self.listing()["notes"][0]["text"], "One thought")
        self.assertEqual(self.listing("garden")["notes"][0]["text"], "Water on Friday")
        self.assertEqual(self.listing("focus")["notes"], [])
        self.assertEqual(self.put(text="Updated", revision=1)[0], 200)
        status, _, raw = self.call("/api/room/forget", {"room_id": "notebook", "note_id": "note1", "expected_revision": 2})
        self.assertEqual(status, 200, raw)
        self.assertFalse(json.loads(raw)["secure_erasure"])
        self.assertEqual(self.listing()["notes"], [])
        self.assertEqual(len(self.listing("garden")["notes"]), 1)
        self.assertEqual(self.put()[0], 409)  # tombstone is not a fresh ID

    def test_restart_and_original_sqlite_readback(self):
        self.assertEqual(self.put(text="Survives restart")[0], 200)
        self.stop()
        with PersonalCompanion(self.db, authority=lambda: self.scope) as store:
            self.assertEqual(RoomNotebook(store).note("notebook", "note1")["text"], "Survives restart")
        self.start()
        self.assertEqual(self.listing()["notes"][0]["revision"], 1)

    def test_snapshot_restore_uses_original_new_store_transaction(self):
        self.assertEqual(self.put()[0], 200)
        self.stop()
        with PersonalCompanion(self.db, authority=lambda: self.scope) as store:
            snapshot = RoomNotebook(store).snapshot()
        self.db = Path(self.tmp.name).resolve() / "restored.sqlite3"
        with PersonalCompanion(self.db, authority=lambda: self.scope) as store:
            self.assertEqual(RoomNotebook(store).restore(snapshot)["restored"], 1)
            with self.assertRaisesRegex(ValueError, "RESTORE_TARGET_NOT_EMPTY"):
                RoomNotebook(store).restore(snapshot)
        self.start()
        self.assertEqual(self.listing()["notes"][0]["text"], "One thought")

    def test_stale_and_concurrent_edits_cannot_overwrite(self):
        self.assertEqual(self.put()[0], 200)
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda text: self.put(text=text, revision=1)[0], ["Left", "Right"]))
        self.assertEqual(sorted(results), [200, 409])
        self.assertEqual(self.listing()["notes"][0]["revision"], 2)
        self.assertEqual(self.put(text="Stale", revision=1)[0], 409)
        self.assertNotEqual(self.listing()["notes"][0]["text"], "Stale")

    def test_ambiguous_response_readback_needs_no_write_retry(self):
        # Do not consume the successful mutation response; recover original state.
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        connection.request("POST", "/api/room/put", json.dumps({"room_id": "notebook", "note_id": "note1", "text": "Lost acknowledgement", "expected_revision": 0}),
                           {"Authorization": "Bearer " + self.token, "Content-Type": "application/json"})
        response = connection.getresponse()
        self.assertEqual(response.status, 200)
        connection.close()
        self.assertEqual(self.listing()["notes"][0]["text"], "Lost acknowledgement")
        self.assertEqual(self.listing()["notes"][0]["revision"], 1)

    def test_auth_origin_host_and_fetch_site_refusals(self):
        body = {"room_id": "notebook"}
        for headers, auth, expected in [({}, False, 401), ({"Authorization": "Bearer wrong"}, True, 401),
             ({"Origin": "https://other.invalid"}, True, 403), ({"Origin": "null"}, True, 403),
             ({"Host": "other.invalid"}, True, 403), ({"Sec-Fetch-Site": "cross-site"}, True, 403)]:
            with self.subTest(headers=headers):
                self.assertEqual(self.call("/api/room/list", body, headers=headers, auth=auth)[0], expected)
        self.assertEqual(self.call("/api/room/list", body, headers={"Origin": self.origin})[0], 200)

    def test_changed_owner_or_space_requires_new_server_session(self):
        self.assertEqual(self.put()[0], 200)
        original = self.scope
        for scope in [CompanionScope("other", "space", "other", True), CompanionScope("owner", "other", "owner", True), CompanionScope("owner", "space", "visitor", False)]:
            self.scope = scope
            self.assertEqual(self.call("/api/room/list", {"room_id": "notebook"})[0], 403)
            self.assertEqual(self.put(text="Wrong scope")[0], 403)
        self.scope = original
        self.assertEqual(self.listing()["notes"][0]["text"], "One thought")

    def test_browser_cannot_supply_authority_or_paths(self):
        for extra in [{"owner_id": "other"}, {"space_id": "other"}, {"database": "../other.db"}, {"owner_present": True}]:
            self.assertEqual(self.call("/api/room/list", dict(room_id="notebook", **extra))[0], 400)
        self.assertEqual(self.listing()["notes"], [])

    def test_invalid_values_are_refused_without_persistence(self):
        cases = [{"room_id": "../garden"}, {"room_id": None}, {"note_id": "garden__note1"},
                 {"note_id": "../other"}, {"note_id": "n" * 41}, {"text": " "}, {"text": "x" * 8001},
                 {"text": None}, {"text": "bad\u202etext"}, {"expected_revision": True},
                 {"expected_revision": -1}, {"expected_revision": 1.5}, {"expected_revision": 2**53}]
        for change in cases:
            data = dict(room_id="notebook", note_id="note1", text="Valid", expected_revision=0)
            data.update(change)
            with self.subTest(change=change):
                self.assertEqual(self.call("/api/room/put", data)[0], 400)
        self.assertEqual(self.listing()["notes"], [])

    def test_unicode_codepoint_limit_and_utf8_http_roundtrip(self):
        for count, expected in ((4001, 200), (8000, 200), (8001, 400)):
            text = "\U0001f600" * count
            body = json.dumps(dict(room_id="notebook", note_id="unicode" + str(count),
                                   text=text, expected_revision=0),
                              ensure_ascii=False).encode("utf-8")
            with self.subTest(codepoints=count):
                self.assertLess(len(body), 32768)
                status, _, raw = self.call("/api/room/put", body)
                self.assertEqual(status, expected, raw)
        rows = self.listing()["notes"]
        self.assertEqual({row["note_id"]: len(row["text"]) for row in rows},
                         {"unicode4001": 4001, "unicode8000": 8000})

    def test_malformed_duplicate_and_nonfinite_json(self):
        for raw in ['{"room_id":"notebook","room_id":"garden"}', '{"room_id":NaN}', '[]', '{', 'null']:
            self.assertEqual(self.call("/api/room/list", raw)[0], 400)
        self.assertEqual(self.call("/api/room/list", "x" * 32769)[0], 413)
        self.assertEqual(self.call("/api/room/list", "{}", headers={"Content-Type": "text/plain"})[0], 415)
        self.assertEqual(self.listing()["notes"], [])

    def test_truncated_body_is_refused(self):
        raw = ("POST /api/room/put HTTP/1.0\r\nHost: 127.0.0.1:" + str(self.port) +
               "\r\nAuthorization: Bearer " + self.token + "\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n{}")
        with socket.create_connection(("127.0.0.1", self.port), timeout=5) as connection:
            connection.sendall(raw.encode())
            connection.shutdown(socket.SHUT_WR)
            self.assertIn(b"400", connection.recv(4096).split(b"\r\n", 1)[0])
        self.assertEqual(self.listing()["notes"], [])

    def test_storage_fault_is_uncertain_and_preserves_previous_note(self):
        self.assertEqual(self.put()[0], 200)
        with patch.object(RoomNotebook, "put", side_effect=OSError("synthetic storage failure")):
            status, _, raw = self.put(text="Not saved", revision=1)
        self.assertEqual(status, 503, raw)
        self.assertIn("UNCONFIRMED", json.loads(raw)["error"])
        self.assertEqual(self.listing()["notes"][0]["text"], "One thought")

    def test_no_native_or_other_mode_endpoints(self):
        for route in ["/api/claim", "/api/callback", "/api/request", "/api/config", "/api/note", "/api/desk/note"]:
            self.assertEqual(self.call(route, {})[0], 404, route)
        data = self.listing()
        self.assertFalse(data["native_installed"])
        self.assertFalse(data["provider_connected"])

    def test_static_assets_have_no_session_and_static_preview_stays_offline(self):
        status, headers, body = self.call("/", method="GET", auth=False)
        self.assertEqual(status, 200)
        self.assertIn(b"room-note-form", body)
        self.assertNotIn(self.token.encode(), body)
        self.assertIn("connect-src 'self'", headers["Content-Security-Policy"])
        self.assertIn("frame-ancestors 'none'", headers["Content-Security-Policy"])
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertNotIn("Access-Control-Allow-Origin", headers)
        static = (ROOT / "examples/companion_home/index.html").read_text(encoding="utf-8")
        self.assertIn("connect-src 'none'", static)
        self.assertNotIn('src="notebook.js"', static)
        self.assertEqual(self.call("/../notes.sqlite3", method="GET")[0], 404)

    def test_companion_mode_is_explicit_and_incompatible_modes_refuse(self):
        self.assertIn("companion_home", inspect.signature(make_server).parameters)
        for value in [1, "true", None]:
            with self.assertRaises(ValueError):
                make_server(self.db, token=self.token, authority=lambda: self.scope, companion_home=value)
        with self.assertRaises(ValueError):
            make_server(self.db, token=self.token, authority=lambda: self.scope, companion_home=True, daily_desk=True)
        self.stop()
        self.start(enabled=False)
        self.assertEqual(self.call("/api/room/list", {"room_id": "notebook"})[0], 404)
        self.assertEqual(self.call("/api/state", method="GET")[0], 200)


if __name__ == "__main__":
    unittest.main()
