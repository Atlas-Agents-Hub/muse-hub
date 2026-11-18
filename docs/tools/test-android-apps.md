# Test Android Apps

**Verify an Android feature on an emulator**

Exercise a real Android flow and capture the screenshots, logs, and performance evidence needed to explain failures.

**Works well with:** Software Engineer, Adversarial Verifier, Product Interface Designer.

## What to bring

- APK or project
- User-flow steps
- Expected screen states

## Setup

1. Prepare the Android SDK, adb target, and application build.

**Access:** Local tools.

## Supported functions

| Function | Use it to |
| --- | --- |
| `android-emulator-qa` | Run and inspect a real Android flow |
| `android-performance` | Capture appropriate CPU, frame, or memory evidence |

## Workflow

1. Install and launch the specified build on the chosen emulator.
2. Run the flow with adb interactions and inspect the UI tree at key steps.
3. Capture screenshots and relevant logcat errors.
4. For a measured performance issue, capture the appropriate frame, CPU, or memory trace and compare a repeatable baseline.

## What you get

- Flow result
- Screenshots and logs
- Performance trace when needed

## Check the result

- The expected final screen and persisted state are present.
- Failures include exact steps, target details, and the tested build.

## Try it

> Use Test Android Apps to verify an Android feature on an emulator. Start from the inputs I provide, follow the setup and workflow, and return flow result, screenshots and logs, performance trace when needed. Verify: The expected final screen and persisted state are present. Failures include exact steps, target details, and the tested build.

## Combine it with

- **Build and verify a mobile experience:** Expo, Testing React Native Apps, Product Design.

## Learn more

- [github.com](https://github.com/openai/plugins)
