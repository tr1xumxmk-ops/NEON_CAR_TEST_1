# Build, flash, and memory notes

## Toolchain

- Arduino IDE 2.x or Arduino CLI.
- ESP32 board package with ESP32-S2 support.
- `ESP32Servo` library.
- Data-capable USB cable.

Open `CyberCar_SPARK_CAR/CyberCar_SPARK_CAR.ino` as the sketch. Arduino builds use the sketch directory for local `.h` files, so do not move headers out into separate folders without updating includes.

## `build_opt.h`

The sketch folder includes:

```text
-DWEBSERVER_MAX_LINE_WAIT=1200
-DWEBSERVER_MAX_HEADER_WAIT=3000
-DWEBSERVER_MAX_URI_LEN=1024
-DWEBSERVER_MAX_LINE_LEN=1024
-DWEBSERVER_MAX_POST_ARG_LEN=2048
```

These definitions are meant for Arduino-ESP32 WebServer versions that expose these limits. If a build reports that one option is unknown or unused, confirm the installed Arduino-ESP32 core and its WebServer implementation rather than blindly changing limits. The project has not been verified against every core version.

## Runtime memory

The UI is embedded as a flash-resident raw string (`PROGMEM`), and avatars are inline SVG/CSS. This avoids loading individual image files from a filesystem. Browser-generated sound runs on the phone/computer, not as audio buffers on the ESP32.

The `/api/state` response includes free heap and uptime. Serial Monitor prints the reset cause and heap at startup. Capture the full serial output if resets recur.

## Build validation

From the repository root:

```bash
python scripts/validate_project.py
```

This verifies portal/preview synchronization, expected face/sound controls, project files, and JavaScript syntax if Node.js is available. It is a static validation step, not an Arduino firmware compile or hardware test.

## Floating mini-companion impact
The always-visible SPARK PAL dock is HTML/CSS/SVG/JavaScript running in the phone or computer browser. Its idle mood timer does **not** run on the ESP32 and the widget adds no new HTTP polling or API routes; it reuses the existing companion state updates and user clicks. The icon's selected SVG is cloned from the existing 20-face library. The new UI is embedded in the same flash-resident `PAGE_HTML` raw string. The current HTML template is approximately 137 KB before compiler compression; verify free flash space and perform a real Arduino build for your board/core combination before publishing a firmware binary.


## PICO companion footprint note

The PICO edition adds inline SVG expression overlay markup, a small browser-side autonomous mood scheduler, Web Audio tone profiles, and beep-only Web Audio support. These run in the browser and do not add an ESP32 polling loop or extra drive requests. The full firmware build/flash size should still be measured using the exact Arduino-ESP32 board/core and build settings before release; this project has not been measured on the user's physical ESP32-S2 Mini in this environment.


## Companion voice update

The current embedded HTML is approximately 209 KB before compiler processing. It contains exactly two floating character profiles (PICO and BEEP), while the separate visual face library retains 20 SVG characters. The browser-only companion adds Web Speech API and Web Audio API functionality; speech and audio availability depend on browser support. It does not add requests to the ESP32 for idle reactions. Validate `index_preview.html` and `captive_portal.h` synchronization with `python scripts/validate_project.py` after every UI change. Flash/RAM use and behavior still need to be verified with the target Arduino-ESP32 build and physical board.
