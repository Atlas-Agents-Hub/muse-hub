# Build a macOS Feature

Implement a native feature and verify it against the application’s interaction and security requirements.

## Bring these inputs

- Swift project and feature brief
- macOS target and required permissions

## 1. Swift

Read [the Swift method](../skills/swift-expert/SKILL.md). Implement the feature using the project architecture and supported Swift APIs.

**Carry forward:** A buildable feature with documented state and concurrency boundaries.

**Check:** The target builds and the feature handles expected state changes.

## 2. Secure Code Guardian

Read [the Secure Code Guardian method](../skills/secure-code-guardian/SKILL.md). Review file access, permissions, data storage, and external inputs.

**Carry forward:** Corrections for concrete security and privacy issues.

**Check:** Access is limited to the required resources and invalid inputs fail safely.

## 3. Software Test Design

Read [the Software Test Design method](../skills/test-master/SKILL.md). Exercise the main interaction, cancellation, and recovery cases.

**Carry forward:** A tested feature and reproducible macOS build instructions.

**Check:** The feature passes its behavior checks on the stated macOS target.

## Check the finished work

- The target builds and the feature handles expected state changes.
- Access is limited to the required resources and invalid inputs fail safely.
- The feature passes its behavior checks on the stated macOS target.

## Finish

A tested feature and reproducible macOS build instructions. The feature passes its behavior checks on the stated macOS target.

## Tools for this workflow

Read [the included tool guides](../../../docs/tools/README.md) when a stage calls for those tools.
