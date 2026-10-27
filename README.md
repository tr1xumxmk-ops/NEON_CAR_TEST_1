
[SPARK_CAR_README_Complete.md](https://github.com/user-attachments/files/33993653/SPARK_CAR_README_Complete.md)
<div align="center">
  <img src="docs/assets/readme/banner.svg" alt="SPARK CAR — Neon Robotics Project" width="100%">

  <h1>SPARK CAR — Neon Robotics & Companion Edition</h1>
  <p><strong>An ESP32-S2 Mini Wi-Fi robot car with a local captive portal, button-based motor control, servo positioning, buzzer support, 20 original SVG faces, and animated PICO & BEEP companions.</strong></p>
  <p>
    <img alt="Platform" src="https://img.shields.io/badge/Platform-ESP32--S2-1769aa?style=for-the-badge&logo=espressif&logoColor=white">
    <img alt="Firmware" src="https://img.shields.io/badge/Firmware-Arduino%20C%2B%2B-008184?style=for-the-badge&logo=arduino&logoColor=white">
    <img alt="Control" src="https://img.shields.io/badge/Control-Local%20Wi--Fi-7857ff?style=for-the-badge">
    <img alt="License" src="https://img.shields.io/badge/License-Apache--2.0-20a464?style=for-the-badge">
  </p>
  <p>
    <a href="docs/index.html">Open browser preview</a> ·
    <a href="WIRING.md">Wiring guide</a> ·
    <a href="HARDWARE_BOM.md">Hardware/BOM</a> ·
    <a href="PUBLISHING.md">Publish to GitHub</a>
  </p>
</div>

> [!WARNING]
> **Prototype hardware.** Test with drive wheels lifted, use a charged and correctly protected battery, and keep a physical battery disconnect accessible. Software stop/brake commands are not a substitute for electrical isolation. Never expose this local HTTP control portal to the public Internet.

## Contents

- [Project overview](#project-overview)
- [Visual preview](#visual-preview)
- [Features and implementation status](#features-and-implementation-status)
- [Hardware list](#hardware-list)
- [Wiring diagrams](#wiring-diagrams)
- [GPIO pin map](#gpio-pin-map)
- [Power and battery safety](#power-and-battery-safety)
- [Install and upload firmware](#install-and-upload-firmware)
- [Connect to the car](#connect-to-the-car)
- [Controls](#controls)
- [Web API](#web-api)
- [PICO, BEEP, and cartoon stories](#pico-beep-and-cartoon-stories)
- [Repository layout](#repository-layout)
- [Troubleshooting](#troubleshooting)
- [GitHub Pages](#github-pages)
- [SPARK Team](#spark-team)
- [Security and privacy](#security-and-privacy)
- [Validation and testing](#validation-and-testing)
- [License and credits](#license-and-credits)

## Project overview

**SPARK CAR** is a hands-on robotics prototype built around an **ESP32-S2 Mini**, an **L298N dual H-bridge driver**, two DC gear motors, and a hobby servo. The ESP32 creates a private Wi-Fi access point and serves the user interface directly from firmware flash. A phone or computer connects to that network and opens the car's dashboard; no home router, cloud account, or Internet connection is needed for normal local control.

The portal pairs physical robot control with a playful interface. The dashboard includes 20 original vector avatars; a separate floating companion selector with **PICO** and **BEEP**; optional browser speech; synthesized sound/music; mini-cartoon scenes; and a project/team introduction. Those visual and audio features run in the browser and are independent of the motor control code.

### At a glance

| Item | Current release |
|---|---|
| Microcontroller | ESP32-S2 Mini-compatible board |
| Motor driver | L298N dual H-bridge module |
| Drive | Two DC gear motors; forward, backward, left, right, stop |
| Control network | ESP32 soft access point; local HTTP at `192.168.4.1` |
| Servo | Hobby servo on configured GPIO 13; requested range 0–180° |
| Hardware horn | Optional buzzer circuit on GPIO 18; wiring must be verified |
| Avatars | 20 inline SVG/CSS character drawings |
| Floating companions | PICO and BEEP, separate character profiles |
| Browser audio | Web Audio effects/music; optional speech synthesis |
| Preview | `docs/index.html`; simulation only, not a physical car controller |

## Visual preview

### Dashboard

![SPARK CAR dashboard preview](docs/assets/readme/dashboard-preview.png)

### Cartoon companion scene

![PICO mini-cartoon scene](docs/assets/readme/cartoon-story.png)

The preview is a browser simulation. When opened locally or via GitHub Pages, it **does not control physical motors or the servo**. The real control page is served from `CyberCar_SPARK_CAR/captive_portal.h` by the ESP32.

## Features and implementation status

| Feature | Status / exact behavior |
|---|---|
| Wi-Fi access point and captive portal | Implemented; OS captive mini-browser behavior differs by phone. Enter `http://192.168.4.1/` manually if needed. |
| Button-based drive | Implemented; hold a direction to drive and release to stop. Arrow keys/WASD are supported on keyboard. |
| Rapid direction changes | Browser coalesces commands; new directions and stop are prioritized over duplicate refreshes. |
| Drive safety timeout | If manual drive refreshes stop, firmware stops after the configured `COMMAND_TIMEOUT_MS` (500 ms by default). |
| Emergency stop | Latches motor stop/brake until the user resumes; hardware disconnect remains the real isolation method. |
| Servo position | Implemented as target angle 0–180°; movement speed and torque depend on the actual servo/load. |
| Speed setting | FAST is continuous digital enable. MEDIUM/SLOW are timed digital on/off bursts, not smooth analog PWM. |
| Hardware buzzer | Firmware generates tones on `BUZZER_PIN` (GPIO18 by default), but an external buzzer/circuit must be wired. A normal L298N module does not include an onboard buzzer. |
| Main face library | 20 inline SVG/CSS faces; no personal photos or remote image downloads. |
| PICO & BEEP | Two independent floating companion profiles, each with its own expressions, dialogue profile and sound palette. |
| Mini-cartoon stories | Code-generated SVG/CSS scenes, including PICO's banana-peel mishap and BEEP's computer/piano stories. These are animations, not prerecorded videos. |
| Random idle behavior | Browser-driven, with reactions to idle time, scrolling, pointer movement, and controller events. Timers may be throttled when the page is in the background. |
| Browser sound/music | Generated locally with Web Audio. Loudness depends on device/browser and the companion volume control. |
| Spoken dialogue | Optional browser Speech Synthesis; available voice, language, and voice quality depend on the device. Autoplay may require a user gesture. |
| Team introduction | Spoken introduction and signature beep can be triggered from the dashboard; team information is also visible as text. |
| AUTO mode | A short timed, **sensorless demonstration**. It is not obstacle avoidance and should only be tried with wheels lifted / in a clear controlled area. |
| Q-learning mode | UI/policy simulation only; this firmware does not run a trained policy and keeps real motors stopped in this mode. |
| RGB LED outputs | Removed. The web page's connection indicator is drawn on screen and does not require a physical LED. |
| Internet/cloud access | Not implemented or recommended. Use the access point locally only. |

## Hardware list

See the detailed [Hardware Bill of Materials](HARDWARE_BOM.md). The primary parts are:

- ESP32-S2 Mini (verify the exact clone-board pinout and power input).
- L298N dual H-bridge module.
- Two DC gear motors and matching chassis/wheels.
- Three-cell LiPo pack in series (3S) as in the described build; pack details must match its chemistry/cell ratings.
- Regulated 5 V buck converter for the ESP32/servo accessory rail, sized for peak/stall demand.
- Hobby servo, compatible with 5 V supply and GPIO 13 signal arrangement.
- Optional buzzer/piezo or a suitable buzzer driver circuit on GPIO 18.
- Proper connectors, insulated wire, power switch/battery disconnect, and a multimeter.

## Wiring diagrams

These are original project-created **schematic illustrations**. They show electrical relationships, not the physical location/orientation of pins on every board revision. Always compare the pin labels on your exact hardware before connecting power.

### 1. Complete system overview

![SPARK CAR system and wiring overview](docs/assets/wiring/system-overview.png)

[Open editable SVG](docs/assets/wiring/system-overview.svg)

### 2. ESP32-S2 Mini signal map

![ESP32-S2 Mini to L298N and accessories pin map](docs/assets/wiring/esp32-l298n-pinmap.png)

[Open editable SVG](docs/assets/wiring/esp32-l298n-pinmap.svg)

### 3. 3S battery and regulated 5 V power distribution

![3S LiPo power distribution](docs/assets/wiring/power-distribution-3s.png)

[Open editable SVG](docs/assets/wiring/power-distribution-3s.svg)

For full step-by-step connections, warnings, and commissioning checks, read **[WIRING.md](WIRING.md)**.

## GPIO pin map

This table is derived from `CyberCar_SPARK_CAR/config.h`. It is only correct for a build wired to these configured pins. If you change pins, update `config.h`, this table, and the drawings together.

| ESP32-S2 GPIO | Firmware symbol | Connect to | Notes |
|---:|---|---|---|
| GPIO 7 | `MOTOR_IN1_PIN` | L298N IN1 | Motor A direction input 1 |
| GPIO 6 | `MOTOR_IN2_PIN` | L298N IN2 | Motor A direction input 2 |
| GPIO 4 | `MOTOR_IN3_PIN` | L298N IN3 | Motor B direction input 1 |
| GPIO 5 | `MOTOR_IN4_PIN` | L298N IN4 | Motor B direction input 2 |
| GPIO 11 | `MOTOR_ENA_PIN` | L298N ENA | Remove ENA jumper if this GPIO drives it |
| GPIO 12 | `MOTOR_ENB_PIN` | L298N ENB | Remove ENB jumper if this GPIO drives it |
| GPIO 13 | `BALL_SERVO_PIN` | Servo signal | Verify connector order and signal tolerance |
| GPIO 18 | `BUZZER_PIN` | Optional buzzer input/driver | Not an onboard L298N feature; do not exceed GPIO current limits |

**Motor direction note:** Which physical motor counts as left/right depends on assembly and output wiring. Raise the wheels for the first test. If the car's direction mapping differs, review motor lead polarity and `INVERT_LEFT_MOTOR` / `INVERT_RIGHT_MOTOR` in `config.h` instead of editing multiple places.

## Power and battery safety

> [!CAUTION]
> The correct wiring depends on the exact L298N module, ESP32-S2 Mini clone, servo, and battery pack. **Do not copy a generic diagram without checking each board's silkscreen and instructions.**

- A standard **3S LiPo** is 11.1 V nominal and 12.6 V fully charged. Use a dedicated 3S balance charger. Never try to charge a 3S pack with a single-cell TP4056/IP5310/power-bank module.
- Feed the battery to the L298N motor supply and to the input of a suitable buck converter as separate branches. Do not feed the L298N's 5 V output into the input of a buck/boost module.
- Use a buck converter whose input rating is above 12.6 V with margin and whose continuous output current is adequate for the ESP32 plus the servo's peak/stall current and all attached accessories. A nominal 5 V, 3–5 A converter is only a sizing starting point, not a guarantee for every servo.
- Before connecting electronics, set the regulator output to **5.00 V using a multimeter**. Connect it only to the ESP32 board's documented 5 V/VBUS input and to accessories rated for that supply.
- Join battery negative, L298N GND, buck input/output GND, ESP32 GND, and servo GND to a common ground. Route motor current separately from sensitive ESP32 power wiring.
- Do **not** connect two 5 V outputs together. For the L298N logic 5 V terminal, follow your exact module's `5V-EN`/regulator jumper documentation. If using external 5 V logic, disable its onboard regulator exactly as directed before connecting the external rail.
- Do not assume an L298N onboard linear regulator has enough spare current or thermal capacity to power the ESP32 and servo. Many modules get hot or experience voltage sag under load.
- Avoid powering through USB and an external 5 V rail simultaneously unless the exact board's power path supports it.
- Never power a motor or servo from ESP32 GPIO or the 3V3 pin. Confirm servo wire colors from its manufacturer; red is usually V+, brown/black usually GND, yellow/orange usually signal.
- Keep a physical battery disconnect accessible. Disconnect power before changing wiring. Use insulated connectors and protect the battery against short circuits.

## Install and upload firmware

### Requirements

- Arduino IDE 2.x or Arduino CLI.
- Arduino-ESP32 **3.x** board package with ESP32-S2 support. This release uses the ESP-IDF 5-style task-watchdog API; compatibility with other core releases must be checked before building.
- `ESP32Servo` library from Arduino Library Manager.
- USB cable that supports data, not charging only.
- Correct board, port, and board-specific flash/USB settings.
- Multimeter for the initial power checks.

### Upload steps

1. Download the release ZIP and extract it, or clone the repository.
2. Open `CyberCar_SPARK_CAR/CyberCar_SPARK_CAR.ino` in Arduino IDE.
3. Keep all `.h` files and `build_opt.h` in the same `CyberCar_SPARK_CAR` sketch directory. Do not open a copied `.ino` separated from its headers.
4. Install `ESP32Servo` if Arduino IDE reports it missing.
5. Edit `CyberCar_SPARK_CAR/config.h`. Change the example access-point password before a public demo. Keep the password at least 8 characters for WPA2 access point mode.
6. Select the ESP32-S2 Mini-compatible board and the correct port.
7. Compile. Resolve any library/core-version errors before wiring the car to a live battery.
8. Upload the firmware.
9. Open **Tools → Serial Monitor**, choose **115200 baud**, and press reset if needed.
10. Review the reset reason and startup messages. If debugging instability, keep the log from startup through the first reboot.

### Default access point

| Setting | Default |
|---|---|
| SSID | `Spark-Car` |
| Sample password | `12345678` (change before sharing/publishing the physical robot) |
| Portal URL | `http://192.168.4.1/` |
| HTTP port | `80` |
| AP address | `192.168.4.1/24` |
| Max client count | `2` |

The password is a sample embedded in `config.h`; publishing the firmware means this default is visible to anyone reading the source. Choose a new password before uploading a public/demo build.

## Connect to the car

1. Raise the car's wheels and make sure the servo/horn cannot snag cables.
2. Power the ESP32 and the motor system using the checked supplies.
3. On the phone/laptop, join Wi-Fi `Spark-Car`. If asked whether to stay connected without Internet, choose to remain connected.
4. Open the normal browser and enter `http://192.168.4.1/` manually if the captive window is unreliable.
5. Test **STOP**, servo, horn (only if hardware is wired), and then each direction briefly.
6. Lower the car only after the directions, stop timeout, and physical power disconnect have been checked.

## Controls

- **Forward / Backward / Left / Right:** hold to move; release to request stop.
- **Stop:** sends a stop request and returns control to Manual mode.
- **Emergency brake:** latches the stop/brake state; use Resume to unlock, then issue a new direction command. Resume does not start the car by itself.
- **Speed:** FAST is continuous digital enable; MEDIUM and SLOW use timed ON/OFF bursts and may feel pulsed. Smooth PWM speed control is not implemented in this version.
- **Servo:** use the slider or presets for target angles 0–180 degrees. A servo can move slowly under load; software only changes the target position.
- **Horn:** sends a request to firmware GPIO 18. This requires an actual buzzer or driver circuit wired to that output.
- **AUTO:** a short sensorless demo sequence; it cannot detect obstacles. Do not use near people, edges, stairs, or fragile objects.
- **Q-learning:** UI simulation only; real motor outputs are held stopped because no reward/observation sensors and trained policy are part of this release.
- **Companion Studio:** PICO and BEEP can animate, talk through available browser voices, play synthesized effects, dance, and perform mini-stories. Use voice/sound toggles to control browser audio.

## Web API

The dashboard uses same-origin HTTP requests to the local ESP32 portal. POST parameters are URL-encoded form fields; responses are JSON. Mutating endpoints check the page `Origin` and validate their accepted fields. This is a local prototype API, not an authenticated Internet-facing service.

| Endpoint | Method | Parameter(s) | Purpose |
|---|---|---|---|
| `/` | GET | — | Serve embedded dashboard HTML |
| `/api/state` | GET | — | Read command, level, mode, estop, servo, heap and uptime status |
| `/api/drive` | POST | `direction=forward\|backward\|left\|right\|stop` | Manual drive button command |
| `/api/speed` | POST | `level=fast\|medium\|slow` | Set drive profile |
| `/api/mode` | POST | `mode=manual\|auto\|qlearning` | Change control mode |
| `/api/servo` | POST | `angle=0..180` | Set servo target angle |
| `/api/horn` | POST | — | Play firmware buzzer pattern |
| `/api/brake` | POST | — | Engage emergency-stop latch |
| `/api/resume` | POST | — | Clear emergency-stop latch, remain stopped |

Sample command body (form-encoded, not raw JSON):

```text
direction=forward
```

Example response:

```json
{"ok":true}
```

The state response is JSON and includes fields such as `command`, `level`, `mode`, `estop`, `servoAngle`, `servoAttached`, `heap`, and `uptime`. See `CyberCar_SPARK_CAR/web_routes.h` for the implemented handlers.

## PICO, BEEP, and cartoon stories

The main Avatar Lab contains 20 original vector characters, while the floating companion selector is intentionally limited to two independent personalities.

### PICO — curious, cute, and clumsy

PICO is a penguin-inspired robot. His first-visit animation begins with sleep, wakes up, waddles closer, nearly trips, recovers, and welcomes the user. Later he may follow scroll/pointer movement, whistle, attempt a song, dance, chase an imaginary cookie, sneeze sparkles, slip on an imaginary banana peel, meet his shadow, become grumpy, or fall asleep.

### BEEP — clever, calm, and a bit too confident

BEEP is a computer/signal character. He can make packet jokes, investigate a pretend bug, attempt an overly precise bow, chase a runaway packet, and perform a piano recital that starts well, goes wrong, and ends with an embarrassed face-covering reaction.

### How the animation and audio work

- Faces are built from inline SVG and CSS; reactions are code-generated animation sequences, not prerecorded video files.
- Sound effects and piano-like sequences are generated with the browser Web Audio API. Optional spoken lines use the browser Speech Synthesis API; the exact voice depends on installed system voices.
- Browsers can block automatic audio until a user clicks/taps. Enable the voice/sound controls after opening the portal.
- Idle timers are approximate. Background tabs and mobile power-saving can throttle them.
- Companion animation/audio runs on the phone or laptop, not the ESP32. It does not issue drive commands; it reacts to the UI/controller state.
- The signature team introduction displays the team information as text and can be spoken by the selected companion.

See [PICO_BEEP_COMPANIONS.md](PICO_BEEP_COMPANIONS.md), [PICO_BEEP_CINEMATIC_BEHAVIOUR.md](PICO_BEEP_CINEMATIC_BEHAVIOUR.md), and [CARTOON_STORIES.md](CARTOON_STORIES.md) for more.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── LICENSE-OVERVIEW.md
├── LICENSE-IMAGES-AND-ASSETS.md
├── NOTICE.md
├── CITATION.cff
├── WIRING.md
├── HARDWARE_BOM.md
├── SECURE_BACKEND.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── PUBLISHING.md
├── BUILD_AND_MEMORY_NOTES.md
├── HEADER_FILES_GUIDE.md
├── FACE_ASSETS_GUIDE.md
├── PICO_BEEP_COMPANIONS.md
├── PICO_BEEP_CINEMATIC_BEHAVIOUR.md
├── CARTOON_STORIES.md
├── DANCE_PARTY.md
├── CyberCar_SPARK_CAR/
│   ├── CyberCar_SPARK_CAR.ino
│   ├── config.h
│   ├── control_types.h
│   ├── motor_driver.h
│   ├── accessories.h
│   ├── car_controller.h
│   ├── secure_backend.h
│   ├── captive_portal.h
│   ├── web_routes.h
│   ├── build_opt.h
│   ├── index_preview.html
│   └── companion-specific guides
├── docs/
│   ├── index.html                  GitHub Pages simulation entry point
│   ├── SPARK_CAR_Neon_Preview.html
│   └── assets/
│       ├── readme/                 Banner, dashboard, story screenshots
│       └── wiring/                 PNG diagrams and editable SVG sources
├── scripts/validate_project.py
└── .github/                         Actions and issue/PR templates
```

## Troubleshooting

| Problem | Likely checks |
|---|---|
| Wi-Fi network does not appear | Confirm startup in Serial Monitor at 115200 baud, battery/supply condition, board power, and SSID in `config.h`. |
| Captive window doesn't open | Join `Spark-Car`, choose “stay connected without Internet,” then enter `http://192.168.4.1/` in a normal browser. |
| Portal shows “link interrupted” | Check that you are connected to the car's AP; open the direct IP; observe Serial Monitor for a reset or brownout. The Pages/local-file preview is simulated and will not connect to hardware. |
| ESP32 reboots when motors/servo move | Measure the regulated 5 V rail under load, charge/check battery, check wire/connector drop, supply servo from a suitable regulator, and inspect the reset reason. |
| Motors don't move | Check charged battery and polarity, L298N VM/GND, motor output terminals, ENA/ENB jumpers, GPIO wiring, emergency latch, mode, and ground continuity. |
| Direction is reversed | Raise wheels; check motor leads and `INVERT_LEFT_MOTOR` / `INVERT_RIGHT_MOTOR` in `config.h`. |
| Servo doesn't move | Verify GPIO13 signal, actual servo power/ground order, 5 V under load, and Serial Monitor. State endpoint reports `servoAttached`. |
| No physical horn sound | Browser sound is not hardware sound. Check GPIO18 to the actual buzzer/driver, common ground, buzzer type, and driver circuit. A standard L298N does not contain a horn. |
| Browser audio is silent | Click/tap once to unlock audio, turn on `SOUNDS`/`VOICE`, check the tab/device volume and chosen audio output, and test in a normal browser. Browser voice availability varies. |
| Buttons work in preview but not on car | GitHub Pages and local HTML are simulations. Upload the Arduino firmware and use `http://192.168.4.1/` on the car's Wi-Fi. |
| Build errors around watchdog APIs | Install a compatible Arduino-ESP32 3.x board package and ESP32-S2 target; report exact core version/error. |

When diagnosing resets, capture the full Serial Monitor output from boot through the restart. Brownout suggests a voltage drop; watchdog/panic text suggests a software/task issue. Do not mask a power problem by simply disabling safety systems.

## GitHub Pages

The website preview lives in `/docs`. To publish it:

1. Push this repository to GitHub.
2. Open **Settings → Pages**.
3. Choose **Deploy from a branch**, branch `main`, folder `/docs`, then **Save**.
4. Check **Actions** for the Pages deployment and use the public URL shown by GitHub.

GitHub Pages runs the simulated dashboard only. It cannot reach your car's AP through the Internet, and the preview intentionally simulates drive commands.

For upload/publish options, see [PUBLISHING.md](PUBLISHING.md). To prevent the earlier 404 issue, keep the contents of this ZIP at the repository root: `README.md`, `LICENSE`, `WIRING.md`, `docs/`, and `CyberCar_SPARK_CAR/` should all be visible in the root file list.

## SPARK Team

The project is presented as an engineering initiative associated with **Al-Iraqia University — College of Engineering — Artificial Intelligence & Robotics Engineering Department**.

| Team member | Project role | Focus |
|---|---|---|
| Haider Nather | Team Lead | Integration, coordination, release planning, verification tracking |
| Ahmed Amjed | AI Developer | AI/ML exploration and future perception/decision experiments; no trained driving policy is claimed in this release |
| Ayat Sayed | System Designer | Interface requirements, subsystem contracts, dashboard/API experience |
| Baraa Fadhel | Robotics Designer | Chassis/mechanical layout, component arrangement, wiring coordination |

Update these role descriptions with the team's approval if responsibilities change. The interface uses vector profile illustrations, not member photographs.

## Security and privacy

- This is a local, plain-HTTP prototype intended only for the ESP32 access point.
- Change the default `Spark-Car` password before a public demo or deployment. Do not add real passwords, Wi-Fi credentials, tokens, or other secrets to Git.
- Do not port-forward the ESP32, bridge it to a public network, or expose the API to the Internet.
- The firmware validates expected command values and checks request `Origin` for state-changing routes. This is not a substitute for encrypted transport or strong user authentication.
- Keep a physical kill switch/disconnect and use safe bench tests. Software emergency stop can fail if the board loses power or the program becomes unresponsive.
- See [SECURITY.md](SECURITY.md) and [SECURE_BACKEND.md](SECURE_BACKEND.md).

## Validation and testing

Run from the repository root:

```bash
python scripts/validate_project.py
```

The script checks the required files, verifies the embedded portal HTML exactly matches the sketch preview and GitHub Pages preview, checks that 20 main avatar buttons and eight sound controls exist, checks PICO/BEEP companion and story markers, and runs JavaScript syntax validation with Node.js when available. GitHub Actions runs the same static checks on pushes and pull requests.

**Validation limits:** Static checks are not a full Arduino compile, electrical inspection, motor bench test, or servo-load test. This release must be compiled using your selected Arduino-ESP32 board package and tested on the actual wiring before normal operation.

## License and credits

- The source code, documentation, and project-created inline avatar/animation assets in this repository are covered by the **Apache License 2.0** unless a file says otherwise. See [`LICENSE`](LICENSE), [`LICENSE-OVERVIEW.md`](LICENSE-OVERVIEW.md), and [`LICENSE-IMAGES-AND-ASSETS.md`](LICENSE-IMAGES-AND-ASSETS.md).
- Arduino-ESP32 and ESP32Servo are third-party dependencies with their own licensing terms. This repository does not relicense those libraries.
- The wiring diagrams in `docs/assets/wiring/` are original project schematics, not manufacturer board photographs. They describe connectivity, not physical pin placement or guaranteed current capacity.
- No carrier PCB, CAD body, manufacturer schematic, or real board photography is included in this release.
- See [`NOTICE.md`](NOTICE.md) for additional attribution and distribution notes.

---

<div align="center">
  <strong>SPARK CAR · Build. Control. Explore.</strong><br>
  <sub>Designed for learning, prototyping, and engineering demonstrations.</sub>
</div>
