[README.md](https://github.com/user-attachments/files/33992621/README.md)
<div align="center">
  <img src="docs/assets/readme/banner.svg" alt="SPARK CAR — Live Companion Edition" width="100%">

  <h1>SPARK CAR — Live Companion Edition</h1>
  <p><strong>An offline-first ESP32-S2 robot car with a neon control portal, 20 original visual avatars, and two independent animated companions: PICO and BEEP, with optional voice and cute synthesized sound effects.</strong></p>

  <p>
    <img alt="Platform" src="https://img.shields.io/badge/Platform-ESP32--S2-1769aa?style=for-the-badge&logo=espressif&logoColor=white">
    <img alt="Firmware" src="https://img.shields.io/badge/Firmware-Arduino%20C%2B%2B-008184?style=for-the-badge&logo=arduino&logoColor=white">
    <img alt="Network" src="https://img.shields.io/badge/Network-Offline--First-7857ff?style=for-the-badge">
    <img alt="License" src="https://img.shields.io/badge/License-Apache--2.0-20a464?style=for-the-badge">
  </p>
  <p><a href="docs/index.html">Open interactive browser preview</a> · <a href="CyberCar_SPARK_CAR/LIVE_COMPANION_GUIDE.md">Live Companion guide</a> · <a href="PICO_BEEP_CINEMATIC_BEHAVIOUR.md">Cinematic companion stories</a> · <a href="WIRING.md">Wiring guide</a></p>
</div>

> [!WARNING]
> **Prototype hardware — use a physical battery disconnect.** Test with the drive wheels lifted clear of the table first. This is a hobby robotics project, not a safety-certified vehicle controller. Software stop/brake commands are not a substitute for electrical isolation.

## 1. Project at a glance

**SPARK CAR** is a locally controlled robot-car project built around an ESP32-S2 Mini and an L298N dual H-bridge motor-driver module. The ESP32 creates its own Wi-Fi access point and serves a responsive dashboard directly from flash. A phone or laptop connects to that access point and controls the car without a home router, cloud account, or Internet connection.

The dashboard includes a main vector-avatar library with 20 visual characters and a separate floating companion selector containing exactly PICO and BEEP. The two companions have distinct personalities, randomized expressions, optional browser voices, and sound palettes. Browser-generated sounds are separate from the physical buzzer attached to the car.

### Implementation status

| Capability | Status in this release |
|---|---|
| ESP32-S2 access point and embedded portal | Implemented; phone OS captive-window behavior varies by device |
| Manual forward / backward / left / right / stop | Implemented with hold-to-drive buttons and a firmware timeout |
| Servo angle control | Implemented, target range 0–180°; physical speed depends on the servo |
| Hardware horn/buzzer route | Implemented on configured `BUZZER_PIN`; verify the actual buzzer wiring |
| 20 original robot faces | Implemented as inline SVG; no photo files or remote image requests required |
| Live companion reactions | Implemented as lightweight CSS/SVG animations; they are not video files or motion sensors |
| Floating companion studio | Exactly two profiles, PICO and BEEP; autonomous random reactions, one-time entry wake/approach animation, bored/sleepy/sleep cycle, optional voices, and sound controls |
| Browser sound and voice | Web Audio generates custom beep/whistle/grumble/piano-like effects; browser Speech Synthesis provides optional spoken lines. Initial sound may require a user gesture due to autoplay policy. |
| Physical RGB LED GPIO control | Removed; the dashboard's small status indicator is software-only |
| AUTO mode | Short timed, sensorless demonstration sequence — **not autonomous navigation or obstacle avoidance** |
| Q-learning mode | UI/simulation mode; this firmware does not implement a trained driving policy and keeps motors stopped in this mode |
| Cloud / public-Internet control | Not implemented and not recommended for this local HTTP portal |
| Carrier PCB / fabrication files | Not included in this edition |

## 2. Dashboard preview

Open the [standalone interactive simulation](docs/index.html) or the [named preview file](docs/SPARK_CAR_Neon_Preview.html). GitHub itself normally displays HTML source instead of executing it; enable **GitHub Pages** from the repository's `/docs` folder to host the preview as a page.

### Cinematic companion story still

The example below is captured from the live, code-generated BEEP piano scene: timed notes, pressed keys, and the embarrassed hide-face reaction are animated inside the page.

![BEEP mini-story — piano recital goes wrong](docs/assets/readme/cinematic-piano.png)

The preview is simulated: it does **not** send commands to a physical car. The actual dashboard is embedded in `CyberCar_SPARK_CAR/captive_portal.h` and served by the ESP32.


## 3. Features

- **Offline-first UI:** the live dashboard's CSS, JavaScript, SVG art, and sound synthesis are embedded in the firmware; no CDN or external image service is needed.
- **Simple directional pad:** hold a direction to drive; release to request stop. Arrow keys and WASD are available on a keyboard; Space requests stop.
- **Latest-command handling:** browser-side command queuing favors the newest direction instead of letting rapid duplicate requests build up indefinitely.
- **Motor safety timeout:** if drive refreshes stop arriving, firmware stops movement after the configured timeout.
- **Servo panel:** angle slider with presets and paced requests.
- **Main Avatar Lab:** 20 original vector characters for the large dashboard display. The independent floating companion selector has exactly two characters, PICO and BEEP; changing the main avatar does not silently replace the selected floating companion.
- **PICO:** a curious, sweet, clumsy penguin-bot that waddles closer on arrival, follows scroll/pointer movement, attempts little songs, whistles, giggles, gets grumpy, becomes bored, and eventually sleeps.
- **BEEP:** a calmer, witty computer/signal character that tells packet and diagnostic jokes, and occasionally stages a piano recital that starts confidently, goes wrong, and ends with him hiding his face in embarrassment.
- **Voice and sound:** optional browser speech synthesis gives PICO and BEEP distinct pitch/rate profiles; Web Audio generates cute beeps, whistle patterns, grumbles, sleepy tones, and piano-like notes. Actual voices depend on the browser and installed voices.
- **Sound Lab:** whistle, boop, twinkle, happy, chirp/giggle, bubble, sleepy, and magic patterns, generated locally. **MAKE SOUND** controls automatic reactions; **PLAY A SOUND** samples an effect; **A LOOK AT THE FACES** jumps to the library.
- **Hardware horn:** the HORN button sends a request to the ESP32 buzzer output. This is separate from browser audio.
- **Request controls:** direction refreshes are coalesced, servo updates are paced, status polling is slower than drive refresh, and the browser times out failed requests rather than reloading the page.
- **Reset diagnostics:** the serial log prints reset reason and free heap during startup.
- **No external media dependencies:** the robot faces are inline SVG/CSS, not photographs or video downloads.

### PICO & BEEP Companion Studio

The floating companion selector contains exactly two personalities. The separate main Avatar Lab remains a library of 20 vector illustrations.

- **PICO:** curious, affectionate, clumsy, noisy, musical in a very questionable way, easily distracted, and sleepy. His page-entry arrival sequence is performed once per page load: he wakes, waddles closer, nearly trips, catches himself, and greets the visitor.
- **BEEP:** calm and clever with computer/signal jokes. A random piano story begins with a lovely little melody, then deliberately hits wrong notes; BEEP becomes embarrassed and covers his face.
- **Voice toggle:** enables spoken dialogue through the browser Speech Synthesis API. PICO uses a higher pitch and faster rate; BEEP uses a lower pitch and calmer rate. Installed voices differ across devices.
- **Sound toggle:** enables locally synthesized Web Audio effects, including chirps, whistles, grumbles, giggle-like beeps, sleepy tones, and piano notes. Browser autoplay rules may require a user click before sound is audible.
- **Team introduction:** speaks the project, Al-Iraqia University, College of Engineering, Artificial Intelligence & Robotics Engineering Department, and team names through the selected voice; a signature beep plays with it.
- **Autonomy:** idle events, scrolling, pointer direction changes, and controller reactions can trigger expressions. Boredom/sleep timers are approximate and can be throttled in background tabs. Companion behavior runs in the browser and does not send motor requests.

See [PICO_BEEP_COMPANIONS.md](PICO_BEEP_COMPANIONS.md) for the full behavior guide.

## 4. Repository map

```text
SPARK_CAR_GitHub_Release/
├── README.md                         Project overview and setup (this file)
├── LICENSE                           Apache License 2.0 for covered software/docs/assets
├── LICENSE-OVERVIEW.md               License scope and usage notes
├── LICENSE-IMAGES-AND-ASSETS.md       Avatar, sound, and preview-asset notes
├── NOTICE.md                         Project/team attribution and asset notes
├── CITATION.cff                      GitHub citation metadata
├── CODE_OF_CONDUCT.md                Community expectations
├── CONTRIBUTING.md                   Contributor workflow
├── PUBLISHING.md                     GitHub upload and Pages instructions
├── SECURITY.md                       Security reporting and deployment cautions
├── SECURE_BACKEND.md                 Local HTTP/API behavior and limitations
├── WIRING.md                         Power, grounding, and pin reference
├── HEADER_FILES_GUIDE.md             Purpose of each firmware header
├── FACE_ASSETS_GUIDE.md              Avatar, animation, and sound design notes
├── BUILD_AND_MEMORY_NOTES.md         Arduino build and flash/RAM notes
├── CONTRIBUTING.md                   Change and validation workflow
├── SECURITY.md                       Security reporting and deployment cautions
├── .github/
│   ├── ISSUE_TEMPLATE/               Bug and feature request forms
│   └── workflows/                    Static project validation
├── CyberCar_SPARK_CAR/
│   ├── CyberCar_SPARK_CAR.ino        Firmware entry point
│   ├── config.h                      Wi-Fi, GPIO, timing, and rate-limit settings
│   ├── control_types.h                Drive/mode types and time helpers
│   ├── motor_driver.h                 L298N digital motor control and direction dead-time
│   ├── accessories.h                  Servo and non-blocking hardware buzzer wrappers
│   ├── car_controller.h               Drive timeout, modes, brake, accessory orchestration
│   ├── captive_portal.h                AP portal and embedded dashboard HTML
│   ├── secure_backend.h                Headers, origin checks, bounded parameter parsing
│   ├── web_routes.h                   HTTP handlers and response generation
│   ├── build_opt.h                    Arduino-ESP32 WebServer build options
│   └── index_preview.html             Standalone preview kept in sync with embedded HTML
├── docs/
│   ├── index.html                     GitHub Pages preview entry point (simulation)
│   ├── SPARK_CAR_Neon_Preview.html    Same standalone preview
│   └── assets/readme/banner.svg       README banner artwork
└── scripts/validate_project.py       HTML sync, avatar/sound, and JS syntax checks
```

## 5. Hardware architecture

```text
Phone / laptop
  └── joins the ESP32-S2 Wi-Fi access point (local only)
      └── HTTP dashboard at http://192.168.4.1/
          ├── validated control/status requests
          └── status polling
              │
              ▼
        ESP32-S2 Mini
          ├── GPIO 7 / 6 / 4 / 5  → L298N IN1..IN4
          ├── GPIO 11 / 12       → L298N ENA / ENB
          ├── GPIO 13            → optional servo signal
          └── GPIO 18            → configured buzzer signal
                                    (only if physically wired)

Battery pack ──┬──> L298N motor supply ──> DC motors
               └──> suitable regulated converter ──> ESP32 / servo rail

All component grounds must be common. Keep motor/servo current out of thin ESP32 power wiring.
```

This project targets an ESP32-S2 Mini and a typical L298N module, but clone boards and L298N modules differ. Verify your exact board pinout and regulator jumper before wiring. A standard L298N module normally does not include an onboard buzzer; firmware tone generation only works if the configured GPIO drives a buzzer circuit.

## 6. Hardware inventory

| Part | Role | Notes |
|---|---|---|
| ESP32-S2 Mini / LOLIN S2 Mini | Wi-Fi AP, local HTTP server, GPIO control | GPIO is 3.3 V logic; GPIO pins are not 5 V tolerant |
| L298N dual H-bridge module | Reverses motor polarity and enables motor channels | Confirm motor supply range, current capability, and `5V-EN`/regulator jumper behavior |
| Two DC gear motors | Chassis propulsion | Motor outputs connect to L298N OUT terminals, not ESP32 pins |
| 3S LiPo pack (as used in the current build) | Main battery | Standard 3S pack is 11.1 V nominal and 12.6 V fully charged; use the correct 3S balance charger and battery protection |
| 5 V regulated supply / buck converter | ESP32 and servo accessory power | Size for servo peak/stall current plus ESP32/Wi-Fi load; measure 5.0 V before connecting |
| Hobby servo | Accessory/ball mechanism | Use a supply rated for the servo; never power motor current from an ESP32 GPIO or 3V3 pin |
| Buzzer or buzzer-driver circuit | Physical horn/tone | `BUZZER_PIN` is GPIO 18 by default; confirm circuit and pin before use |

> **Power note:** Do not assume that the L298N module's onboard 5 V regulator can safely power the ESP32 and a servo. Its spare current and thermal capacity vary by module. For a 3S LiPo, use a suitable converter from the battery for the 5 V accessory rail. Do not connect two 5 V outputs together. See [WIRING.md](WIRING.md).

## 7. Pin map

Pin mapping comes from `CyberCar_SPARK_CAR/config.h` and must be verified against the actual wiring before power-up.

| ESP32-S2 GPIO | Configuration symbol | Destination |
|---:|---|---|
| GPIO 7 | `MOTOR_IN1_PIN` | L298N IN1 |
| GPIO 6 | `MOTOR_IN2_PIN` | L298N IN2 |
| GPIO 4 | `MOTOR_IN3_PIN` | L298N IN3 |
| GPIO 5 | `MOTOR_IN4_PIN` | L298N IN4 |
| GPIO 11 | `MOTOR_ENA_PIN` | L298N ENA; remove ENA jumper only if this GPIO drives ENA |
| GPIO 12 | `MOTOR_ENB_PIN` | L298N ENB; remove ENB jumper only if this GPIO drives ENB |
| GPIO 13 | `BALL_SERVO_PIN` | Servo signal |
| GPIO 18 | `BUZZER_PIN` | Buzzer circuit signal, if connected |
| — | — | No physical RGB LED output is used in this edition |

Update `config.h`, wiring notes, and this table together whenever a pin is changed.

## 8. Install and run

### Requirements

- Arduino IDE 2.x or Arduino CLI with the Arduino-ESP32 **3.x** board package (the firmware uses the ESP-IDF 5-style task-watchdog API) and ESP32-S2 support.
- An ESP32-S2 Mini-compatible board definition.
- The **ESP32Servo** library.
- A data-capable USB cable and the correct board/port selection.

### Upload

1. Download the repository ZIP or clone the repository.
2. Open `CyberCar_SPARK_CAR/CyberCar_SPARK_CAR.ino` in Arduino IDE. **Keep all `.h` files and `build_opt.h` in that same sketch folder.**
3. Install `ESP32Servo` from Library Manager if prompted.
4. Select your ESP32-S2 Mini-compatible board and serial port.
5. Review `config.h`, especially the Wi-Fi password, motor pin mapping, servo pin, and buzzer pin.
6. Compile and upload. If your Arduino-ESP32 core rejects one of the `build_opt.h` definitions, check the core version and WebServer hardening options; see [BUILD_AND_MEMORY_NOTES.md](BUILD_AND_MEMORY_NOTES.md).
7. Open Serial Monitor at **115200 baud**.
8. Join Wi-Fi `Spark-Car`, then navigate to `http://192.168.4.1/` in a normal browser. The default example password in `config.h` is `12345678`; **change it before deployment or public demonstration**.
9. Raise the wheels before the first motion test. Keep a physical battery disconnect within reach.

The network is local-only. Phones may show “Connected without Internet”; that is expected. The OS may or may not open its captive mini-browser automatically. Enter the IP manually if needed.

## Companion Studio

The floating companion can be changed independently from the large face library. See [COMPANION_STUDIO.md](CyberCar_SPARK_CAR/COMPANION_STUDIO.md) for character personalities, autonomous behavior, generated beep sounds, scroll peeks, and the team beep signature. All companion logic is browser-side only and never sends motor commands.

## 9. Modes and safety behavior

- **Manual:** hold a direction button to drive; release or press STOP to stop. A firmware timeout stops motion if refresh messages stop arriving.
- **FAST / MEDIUM / SLOW:** FAST uses continuous digital enable. MEDIUM and SLOW use timed digital bursts; they are not analog PWM and can feel pulsed or jerky.
- **AUTO demo:** a short, sensorless timed sequence. It does not detect obstacles and must not be described as self-driving.
- **Q-learning UI mode:** there is no trained Q-learning driving model in this firmware. The real motors are held stopped in this mode while the UI presents a simulation concept.
- **Emergency brake:** software latch that stops/blocks normal drive commands. It is not a safety-rated hardware brake. Use a physical battery switch to isolate power.
- **Lost web connection:** the firmware command timeout is the final software fallback for manual drive; it is not a substitute for safe power wiring.

## 10. Local API reference

The dashboard uses same-origin HTTP requests to the ESP32. Input arguments are form-encoded parameters; successful and failed handlers return JSON responses. This release does **not** accept arbitrary executable code or evaluate user-supplied JavaScript.

| Method | Endpoint | Parameter(s) | Purpose |
|---|---|---|---|
| `GET` | `/` | — | Embedded dashboard |
| `GET` | `/api/state` | — | Current command/mode/servo/heap/uptime JSON state |
| `POST` | `/api/drive` | `direction=forward\|backward\|left\|right\|stop` | Named direction command |
| `POST` | `/api/speed` | `level=fast\|medium\|slow` | Drive profile |
| `POST` | `/api/mode` | `mode=manual\|auto\|qlearning` | Operating mode |
| `POST` | `/api/servo` | `angle=0..180` | Servo target angle |
| `POST` | `/api/horn` | — | Hardware buzzer sequence |
| `POST` | `/api/brake` | — | Latch emergency stop |
| `POST` | `/api/resume` | — | Release brake and remain stopped |

Requests originating outside the expected local portal `Origin` are rejected. Query arguments are validated/whitelisted and request classes are paced. This is useful hardening for a local prototype, **not security suitable for public Internet exposure**. More details: [SECURE_BACKEND.md](SECURE_BACKEND.md).

## 11. SPARK Team

The project is presented as an engineering effort associated with **Al-Iraqia University — College of Engineering — Artificial Intelligence & Robotics Engineering**. Team cards in the dashboard use technical vector-style illustrations rather than member photographs.

| Team member | Project role | Focus |
|---|---|---|
| Haider Nather | Team Lead | Integration, coordination, release planning, verification tracking |
| Ahmed Amjed | AI Developer | AI/ML exploration and future perception/decision experiments; no trained driving policy is claimed in this release |
| Ayat Sayed | System Designer | Interface requirements, subsystem contracts, dashboard and API experience |
| Baraa Fadhel | Robotics Designer | Chassis/mechanical layout, component arrangement and wiring coordination |

Role descriptions are project-maintenance guidance and can be updated by the team. Use only approved likenesses if photographs are ever added.

## 12. Validation and known limitations

Run the repository's static checks from the root:

```bash
python scripts/validate_project.py
```

The check verifies the embedded portal matches the standalone preview, checks expected avatar/sound elements, and runs JavaScript syntax validation with Node.js when available. GitHub Actions runs the same checks on pushes and pull requests.

**Validation boundary:** This repository has been statically checked, but the firmware has not been compiled with every Arduino-ESP32 version or bench-tested on every ESP32-S2 Mini/L298N clone. CI is not a substitute for a hardware test. Build/flash and wiring verification remain required before driving.

## 13. Contributing

Bug reports and focused improvements are welcome. Include the ESP32 board/core version, wiring changes, exact reproduction steps, and relevant Serial Monitor output. Never attach Wi-Fi passwords, private keys, or other secrets. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

## License

Software, documentation, and project-created inline vector assets are licensed under Apache-2.0; see [`LICENSE`](LICENSE) and [`LICENSE-OVERVIEW.md`](LICENSE-OVERVIEW.md). There are no carrier PCB design files in this edition. If hardware files are added later, their licensing scope should be documented separately.


## PICO & BEEP Companion Personalities

The floating companion selector intentionally contains only two characters:

- **PICO** — a cute, curious, clumsy penguin-bot that waddles, runs in place, tries to sing, whistles, giggles, gets grumpy, becomes bored, and falls asleep.
- **BEEP** — a calmer and witty signal/computer companion. He comments on packets and diagnostics, tells gentle technology jokes, attempts a piano performance, plays well at first, then hits wrong notes and hides his face in embarrassment.

The companion uses inline SVG/CSS for face expressions and animation, Web Audio API for custom beeps and little piano melodies, and optional browser speech synthesis for voice lines. The available voice depends on the browser and operating system; the app picks a best-effort English voice and adjusts pitch/rate to distinguish PICO from BEEP. Click **VOICE: OFF** to enable their spoken lines and **SOUNDS: ON/OFF** to control effects. Browser audio can require a user gesture.

On entry the companion shows one wake-up/approach animation. Later idle behavior can progress through boredom, sleepiness, and sleep, while scrolling and movement can trigger reactions. Random companion behavior is browser-only: it does not send motor-control requests.

The team-introduction button reads the project, university, department, and team names aloud with the selected character's voice when speech synthesis is supported, then plays a short signature beep.

## Cinematic PICO & BEEP companions

The floating companion now includes short, scripted mini-scenes made from SVG/CSS character motion, a staged piano keyboard with synchronized key presses, browser-generated notes, and optional browser speech. PICO has a wake-up/waddle/singing story; BEEP has a confident piano recital that deliberately goes wrong, followed by an embarrassed face-covering beat. Random idle behavior continues while the page is visible. Routine movement feedback is shown through subtle facial motion rather than a toast on every command.

**Audio note:** Web Audio and speech synthesis are subject to browser autoplay restrictions. After opening the page, interact once to unlock audio; then the enabled companion can talk and play generated sounds. Voice quality depends on installed system voices. Animations are code-generated live scenes, not a prerecorded video file.

### Latest companion polish
- Louder browser-generated sound effects and music, with controlled output and a 50–150% volume slider.
- Additional autonomous PICO/BEEP dialogue, emotions, and animated idle actions.
- Music volume affects browser audio only, not the physical buzzer or motor wiring.
