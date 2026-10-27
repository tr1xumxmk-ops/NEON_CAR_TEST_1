[SPARK_CAR_LICENSE_Apache_2.0.txt](https://github.com/user-attachments/files/33993857/SPARK_CAR_LICENSE_Apache_2.0.txt)<img width="1800" height="1000" alt="SPARK_CAR_3S_Power_Distribution" src="https://github.com/user-attachments/assets/99dab88f-8839-4e93-8bfa-38d3c84917b1" /><img width="1800" height="1000" alt="SPARK_CAR_System_Wiring_Diagram" src="https://github.com/user-attachments/assets/a928fb25-375e-4718-b7b0-e8bff95098db" />
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

![Uploading SPARK_CAR_System<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1000" viewBox="0 0 1800 1000"><defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071321"/><stop offset="1" stop-color="#19132a"/></linearGradient>
 <marker id="aC" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#42e8ff"/></marker>
 <marker id="aP" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#ff53c8"/></marker>
 <marker id="aL" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#c6ff59"/></marker>
 <marker id="aO" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#ffbc66"/></marker>
 <style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#eaf1ff}.title{font-size:36px;font-weight:800;letter-spacing:.5px}.sub{font-size:17px;fill:#9caecb}.h{font-size:23px;font-weight:800}.b{font-size:18px}.s{font-size:15px;fill:#9caecb}.xs{font-size:13px;fill:#9caecb}.lab{font-size:14px;font-weight:800;letter-spacing:.5px}</style>
 </defs><rect width="100%" height="100%" fill="url(#bg)"/>
 <g opacity=".10" stroke="#5b7398" stroke-width="1"><path d="M0 0 V1000"/><path d="M60 0 V1000"/><path d="M120 0 V1000"/><path d="M180 0 V1000"/><path d="M240 0 V1000"/><path d="M300 0 V1000"/><path d="M360 0 V1000"/><path d="M420 0 V1000"/><path d="M480 0 V1000"/><path d="M540 0 V1000"/><path d="M600 0 V1000"/><path d="M660 0 V1000"/><path d="M720 0 V1000"/><path d="M780 0 V1000"/><path d="M840 0 V1000"/><path d="M900 0 V1000"/><path d="M960 0 V1000"/><path d="M1020 0 V1000"/><path d="M1080 0 V1000"/><path d="M1140 0 V1000"/><path d="M1200 0 V1000"/><path d="M1260 0 V1000"/><path d="M1320 0 V1000"/><path d="M1380 0 V1000"/><path d="M1440 0 V1000"/><path d="M1500 0 V1000"/><path d="M1560 0 V1000"/><path d="M1620 0 V1000"/><path d="M1680 0 V1000"/><path d="M1740 0 V1000"/><path d="M0 0 H1800"/><path d="M0 60 H1800"/><path d="M0 120 H1800"/><path d="M0 180 H1800"/><path d="M0 240 H1800"/><path d="M0 300 H1800"/><path d="M0 360 H1800"/><path d="M0 420 H1800"/><path d="M0 480 H1800"/><path d="M0 540 H1800"/><path d="M0 600 H1800"/><path d="M0 660 H1800"/><path d="M0 720 H1800"/><path d="M0 780 H1800"/><path d="M0 840 H1800"/><path d="M0 900 H1800"/><path d="M0 960 H1800"/></g>
 <text x="54" y="64" class="title">SPARK CAR — SYSTEM OVERVIEW</text><text x="56" y="96" class="sub">How the browser, ESP32 firmware, motor driver, and accessories work together</text><rect x="60" y="175" width="300" height="170" rx="18" fill="#111c30" stroke="#42e8ff" stroke-width="2"/><text x="80" y="209" class="h">PHONE / LAPTOP</text><path d="M78 224 H342" stroke="#42e8ff" stroke-width="2" opacity=".75"/><text x="80" y="255" class="b">Join Spark-Car Wi-Fi</text><text x="80" y="282" class="b">Open http://192.168.4.1/</text><text x="80" y="309" class="b">Dashboard sends local HTTP commands</text><rect x="470" y="175" width="340" height="170" rx="18" fill="#111c30" stroke="#42e8ff" stroke-width="2"/><text x="490" y="209" class="h">ESP32-S2 MINI</text><path d="M488 224 H792" stroke="#42e8ff" stroke-width="2" opacity=".75"/><text x="490" y="255" class="b">Wi-Fi access point + web server</text><text x="490" y="282" class="b">Validate command / state request</text><text x="490" y="309" class="b">GPIO control and safety timeout</text><rect x="920" y="175" width="330" height="170" rx="18" fill="#111c30" stroke="#ff53c8" stroke-width="2"/><text x="940" y="209" class="h">L298N DRIVER</text><path d="M938 224 H1232" stroke="#ff53c8" stroke-width="2" opacity=".75"/><text x="940" y="255" class="b">IN1–IN4: motor direction</text><text x="940" y="282" class="b">ENA / ENB: enable inputs</text><text x="940" y="309" class="b">OUT terminals drive DC motors</text><rect x="1360" y="155" width="370" height="120" rx="18" fill="#10251f" stroke="#c6ff59" stroke-width="2"/><text x="1380" y="189" class="h">MOTOR A</text><path d="M1378 204 H1712" stroke="#c6ff59" stroke-width="2" opacity=".75"/><text x="1380" y="235" class="b">L298N OUT1 / OUT2</text><rect x="1360" y="300" width="370" height="120" rx="18" fill="#10251f" stroke="#c6ff59" stroke-width="2"/><text x="1380" y="334" class="h">MOTOR B</text><path d="M1378 349 H1712" stroke="#c6ff59" stroke-width="2" opacity=".75"/><text x="1380" y="380" class="b">L298N OUT3 / OUT4</text><path d="M360 260 H470" fill="none" stroke="#42e8ff" stroke-width="5" marker-end="url(#aC)"/><text x="374" y="242" class="lab" fill="#42e8ff">LOCAL WI-FI</text><path d="M810 260 H920" fill="none" stroke="#ff53c8" stroke-width="5" marker-end="url(#aP)"/><text x="824" y="242" class="lab" fill="#ff53c8">GPIO SIGNALS</text><path d="M1250 225 H1300 V215 H1360" fill="none" stroke="#c6ff59" stroke-width="4" marker-end="url(#aL)"/><path d="M1250 290 H1300 V360 H1360" fill="none" stroke="#c6ff59" stroke-width="4" marker-end="url(#aL)"/><rect x="470" y="465" width="340" height="160" rx="18" fill="#111c30" stroke="#9a83ff" stroke-width="2"/><text x="490" y="499" class="h">SERVO</text><path d="M488 514 H792" stroke="#9a83ff" stroke-width="2" opacity=".75"/><text x="490" y="545" class="b">GPIO13 = signal</text><text x="490" y="572" class="b">Power from regulated servo rail</text><rect x="920" y="465" width="330" height="160" rx="18" fill="#111c30" stroke="#ffbc66" stroke-width="2"/><text x="940" y="499" class="h">OPTIONAL BUZZER</text><path d="M938 514 H1232" stroke="#ffbc66" stroke-width="2" opacity=".75"/><text x="940" y="545" class="b">GPIO18 = control signal</text><text x="940" y="572" class="b">Add suitable buzzer/driver circuit</text><rect x="1360" y="485" width="370" height="125" rx="18" fill="#111c30" stroke="#5799ff" stroke-width="2"/><text x="1380" y="519" class="h">POWER SYSTEM</text><path d="M1378 534 H1712" stroke="#5799ff" stroke-width="2" opacity=".75"/><text x="1380" y="565" class="b">3S battery → L298N motor rail</text><text x="1380" y="592" class="b">3S battery → 5 V buck for accessories</text><path d="M640 345 V405 H640 V465" fill="none" stroke="#9a83ff" stroke-width="3" stroke-dasharray="7 6" marker-end="url(#aC)"/><path d="M750 345 V420 H1085 V465" fill="none" stroke="#ffbc66" stroke-width="3" stroke-dasharray="7 6" marker-end="url(#aO)"/><rect x="60" y="705" width="1670" height="150" rx="22" fill="#12172a" stroke="#ff53c8" stroke-width="2"/><text x="90" y="748" class="h">PICO &amp; BEEP — BROWSER-ONLY COMPANIONS</text><text x="90" y="784" class="b">SVG/CSS expressions • mini-cartoon stories • Web Audio beeps/music • optional browser speech</text><text x="90" y="820" class="s">Companion animations run on the phone/laptop. They do not send extra motor commands and are not physical motion sensors.</text><rect x="60" y="890" width="1670" height="55" rx="14" fill="#301722" stroke="#ff657a" stroke-width="2"/><text x="85" y="924" class="lab" fill="#ff657a">SAFETY:</text><text x="170" y="924" class="b">Wiring details and common-ground requirements are shown in the power diagram; verify your exact board/module revision.</text></svg>_Wiring_Diagram.svg…]()


[Open editable SVG](docs/assets/wiring/system-overview.svg)

### 2. ESP32-S2 Mini signal map

<img width="1800" height="1030" alt="SPARK_CAR_ESP32_GPIO_Pinmap" src="https://github.com/user-attachments/assets/08d43b37-7833-4998-9444-499f012739f3" />
<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1030" viewBox="0 0 1800 1030"><defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071321"/><stop offset="1" stop-color="#19132a"/></linearGradient>
 <marker id="aC" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#42e8ff"/></marker>
 <marker id="aP" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#ff53c8"/></marker>
 <marker id="aL" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#c6ff59"/></marker>
 <marker id="aO" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#ffbc66"/></marker>
 <style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#eaf1ff}.title{font-size:36px;font-weight:800;letter-spacing:.5px}.sub{font-size:17px;fill:#9caecb}.h{font-size:23px;font-weight:800}.b{font-size:18px}.s{font-size:15px;fill:#9caecb}.xs{font-size:13px;fill:#9caecb}.lab{font-size:14px;font-weight:800;letter-spacing:.5px}</style>
 </defs><rect width="100%" height="100%" fill="url(#bg)"/>
 <g opacity=".10" stroke="#5b7398" stroke-width="1"><path d="M0 0 V1030"/><path d="M60 0 V1030"/><path d="M120 0 V1030"/><path d="M180 0 V1030"/><path d="M240 0 V1030"/><path d="M300 0 V1030"/><path d="M360 0 V1030"/><path d="M420 0 V1030"/><path d="M480 0 V1030"/><path d="M540 0 V1030"/><path d="M600 0 V1030"/><path d="M660 0 V1030"/><path d="M720 0 V1030"/><path d="M780 0 V1030"/><path d="M840 0 V1030"/><path d="M900 0 V1030"/><path d="M960 0 V1030"/><path d="M1020 0 V1030"/><path d="M1080 0 V1030"/><path d="M1140 0 V1030"/><path d="M1200 0 V1030"/><path d="M1260 0 V1030"/><path d="M1320 0 V1030"/><path d="M1380 0 V1030"/><path d="M1440 0 V1030"/><path d="M1500 0 V1030"/><path d="M1560 0 V1030"/><path d="M1620 0 V1030"/><path d="M1680 0 V1030"/><path d="M1740 0 V1030"/><path d="M0 0 H1800"/><path d="M0 60 H1800"/><path d="M0 120 H1800"/><path d="M0 180 H1800"/><path d="M0 240 H1800"/><path d="M0 300 H1800"/><path d="M0 360 H1800"/><path d="M0 420 H1800"/><path d="M0 480 H1800"/><path d="M0 540 H1800"/><path d="M0 600 H1800"/><path d="M0 660 H1800"/><path d="M0 720 H1800"/><path d="M0 780 H1800"/><path d="M0 840 H1800"/><path d="M0 900 H1800"/><path d="M0 960 H1800"/><path d="M0 1020 H1800"/></g>
 <text x="54" y="64" class="title">ESP32-S2 MINI — GPIO WIRING MAP</text><text x="56" y="96" class="sub">Exact signal names from config.h • table is intentionally easier to verify than physical pin placement</text><rect x="70" y="150" width="1660" height="676" rx="18" fill="#111c30" stroke="#425574" stroke-width="2"/><rect x="71" y="151" width="1658" height="64" rx="17" fill="#182943"/><text x="94" y="191" class="h">ESP32-S2 GPIO</text><text x="464" y="191" class="h">L298N / accessory connection</text><text x="954" y="191" class="h">Purpose / notes</text><rect x="72" y="214" width="1656" height="68" fill="#152138"/><path d="M70 282 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="231" width="10" height="34" rx="5" fill="#42e8ff"/><text x="114" y="257" class="h">GPIO 7</text><text x="464" y="257" class="b">L298N IN1</text><text x="954" y="257" class="b">Motor A direction input 1</text><path d="M70 350 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="299" width="10" height="34" rx="5" fill="#ff53c8"/><text x="114" y="325" class="h">GPIO 6</text><text x="464" y="325" class="b">L298N IN2</text><text x="954" y="325" class="b">Motor A direction input 2</text><rect x="72" y="350" width="1656" height="68" fill="#152138"/><path d="M70 418 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="367" width="10" height="34" rx="5" fill="#9a83ff"/><text x="114" y="393" class="h">GPIO 4</text><text x="464" y="393" class="b">L298N IN3</text><text x="954" y="393" class="b">Motor B direction input 1</text><path d="M70 486 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="435" width="10" height="34" rx="5" fill="#ffbc66"/><text x="114" y="461" class="h">GPIO 5</text><text x="464" y="461" class="b">L298N IN4</text><text x="954" y="461" class="b">Motor B direction input 2</text><rect x="72" y="486" width="1656" height="68" fill="#152138"/><path d="M70 554 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="503" width="10" height="34" rx="5" fill="#c6ff59"/><text x="114" y="529" class="h">GPIO 11</text><text x="464" y="529" class="b">L298N ENA</text><text x="954" y="529" class="b">Remove ENA jumper if GPIO11 controls this pin</text><path d="M70 622 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="571" width="10" height="34" rx="5" fill="#62f7b2"/><text x="114" y="597" class="h">GPIO 12</text><text x="464" y="597" class="b">L298N ENB</text><text x="954" y="597" class="b">Remove ENB jumper if GPIO12 controls this pin</text><rect x="72" y="622" width="1656" height="68" fill="#152138"/><path d="M70 690 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="639" width="10" height="34" rx="5" fill="#42e8ff"/><text x="114" y="665" class="h">GPIO 13</text><text x="464" y="665" class="b">Servo signal</text><text x="954" y="665" class="b">Signal wire only; servo power comes from regulated rail</text><path d="M70 758 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="707" width="10" height="34" rx="5" fill="#ffbc66"/><text x="114" y="733" class="h">GPIO 18</text><text x="464" y="733" class="b">Optional buzzer / driver input</text><text x="954" y="733" class="b">External buzzer circuit required; not built into normal L298N</text><rect x="72" y="758" width="1656" height="68" fill="#152138"/><path d="M70 826 H1730" stroke="#31435e" stroke-width="1"/><rect x="88" y="775" width="10" height="34" rx="5" fill="#5799ff"/><text x="114" y="801" class="h">GND</text><text x="464" y="801" class="b">All module grounds</text><text x="954" y="801" class="b">ESP32, L298N, buck converter, servo and buzzer circuit</text><rect x="70" y="865" width="800" height="95" rx="16" fill="#301722" stroke="#ff657a" stroke-width="2"/><text x="95" y="899" class="h" fill="#ff657a">ENA / ENB JUMPERS</text><text x="95" y="931" class="b">Remove jumper caps when GPIO11 / GPIO12 provide enable signals.</text><rect x="900" y="865" width="830" height="95" rx="16" fill="#172838" stroke="#42e8ff" stroke-width="2"/><text x="925" y="899" class="h" fill="#42e8ff">3.3 V GPIO</text><text x="925" y="931" class="b">Never feed 5 V into an ESP32 GPIO. GPIO18 needs a suitable buzzer circuit.</text><text x="70" y="1000" class="s">GPIO numbers are from this release&#39;s config.h. This is a logical mapping, not the physical pin layout of every S2 Mini clone.</text></svg>

[Open editable SVG](docs/assets/wiring/esp32-l298n-pinmap.svg)

### 3. 3S battery and regulated 5 V power distribution

![Uploading SPARK_CAR_3S_Power<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1000" viewBox="0 0 1800 1000"><defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071321"/><stop offset="1" stop-color="#19132a"/></linearGradient>
 <marker id="aC" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#42e8ff"/></marker>
 <marker id="aP" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#ff53c8"/></marker>
 <marker id="aL" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#c6ff59"/></marker>
 <marker id="aO" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0 L9 5 L0 10Z" fill="#ffbc66"/></marker>
 <style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#eaf1ff}.title{font-size:36px;font-weight:800;letter-spacing:.5px}.sub{font-size:17px;fill:#9caecb}.h{font-size:23px;font-weight:800}.b{font-size:18px}.s{font-size:15px;fill:#9caecb}.xs{font-size:13px;fill:#9caecb}.lab{font-size:14px;font-weight:800;letter-spacing:.5px}</style>
 </defs><rect width="100%" height="100%" fill="url(#bg)"/>
 <g opacity=".10" stroke="#5b7398" stroke-width="1"><path d="M0 0 V1000"/><path d="M60 0 V1000"/><path d="M120 0 V1000"/><path d="M180 0 V1000"/><path d="M240 0 V1000"/><path d="M300 0 V1000"/><path d="M360 0 V1000"/><path d="M420 0 V1000"/><path d="M480 0 V1000"/><path d="M540 0 V1000"/><path d="M600 0 V1000"/><path d="M660 0 V1000"/><path d="M720 0 V1000"/><path d="M780 0 V1000"/><path d="M840 0 V1000"/><path d="M900 0 V1000"/><path d="M960 0 V1000"/><path d="M1020 0 V1000"/><path d="M1080 0 V1000"/><path d="M1140 0 V1000"/><path d="M1200 0 V1000"/><path d="M1260 0 V1000"/><path d="M1320 0 V1000"/><path d="M1380 0 V1000"/><path d="M1440 0 V1000"/><path d="M1500 0 V1000"/><path d="M1560 0 V1000"/><path d="M1620 0 V1000"/><path d="M1680 0 V1000"/><path d="M1740 0 V1000"/><path d="M0 0 H1800"/><path d="M0 60 H1800"/><path d="M0 120 H1800"/><path d="M0 180 H1800"/><path d="M0 240 H1800"/><path d="M0 300 H1800"/><path d="M0 360 H1800"/><path d="M0 420 H1800"/><path d="M0 480 H1800"/><path d="M0 540 H1800"/><path d="M0 600 H1800"/><path d="M0 660 H1800"/><path d="M0 720 H1800"/><path d="M0 780 H1800"/><path d="M0 840 H1800"/><path d="M0 900 H1800"/><path d="M0 960 H1800"/></g>
 <text x="54" y="64" class="title">POWER DISTRIBUTION — 3S LiPo</text><text x="56" y="96" class="sub">Branch the battery into motor power and regulated accessory power; join all grounds at a common reference</text><rect x="70" y="205" width="330" height="205" rx="18" fill="#111c30" stroke="#ffbc66" stroke-width="2"/><text x="90" y="239" class="h">3S LiPo BATTERY</text><path d="M88 254 H382" stroke="#ffbc66" stroke-width="2" opacity=".75"/><text x="90" y="285" class="b">11.1 V nominal</text><text x="90" y="312" class="b">12.6 V full charge</text><text x="90" y="339" class="b">Correct 3S balance charger</text><text x="90" y="366" class="b">Physical disconnect recommended</text><rect x="575" y="165" width="400" height="190" rx="18" fill="#111c30" stroke="#ff53c8" stroke-width="2"/><text x="595" y="199" class="h">L298N MOTOR RAIL</text><path d="M593 214 H957" stroke="#ff53c8" stroke-width="2" opacity=".75"/><text x="595" y="245" class="b">Battery + → VM / motor supply</text><text x="595" y="272" class="b">Battery − → L298N GND</text><text x="595" y="299" class="b">OUT pairs → DC motors</text><rect x="575" y="490" width="400" height="205" rx="18" fill="#111c30" stroke="#c6ff59" stroke-width="2"/><text x="595" y="524" class="h">5 V BUCK CONVERTER</text><path d="M593 539 H957" stroke="#c6ff59" stroke-width="2" opacity=".75"/><text x="595" y="570" class="b">IN+ ← battery +</text><text x="595" y="597" class="b">IN− ← battery −</text><text x="595" y="624" class="b">Measure OUT = 5.00 V first</text><text x="595" y="651" class="b">Continuous current sized for load</text><rect x="1170" y="135" width="560" height="145" rx="18" fill="#111c30" stroke="#42e8ff" stroke-width="2"/><text x="1190" y="169" class="h">ESP32-S2 MINI</text><path d="M1188 184 H1712" stroke="#42e8ff" stroke-width="2" opacity=".75"/><text x="1190" y="215" class="b">Regulated 5 V → documented 5V/VBUS input</text><text x="1190" y="242" class="b">GND → common ground</text><rect x="1170" y="325" width="560" height="145" rx="18" fill="#111c30" stroke="#9a83ff" stroke-width="2"/><text x="1190" y="359" class="h">SERVO</text><path d="M1188 374 H1712" stroke="#9a83ff" stroke-width="2" opacity=".75"/><text x="1190" y="405" class="b">V+ → regulated rail matched to servo</text><text x="1190" y="432" class="b">Signal → GPIO13 • GND → common ground</text><rect x="1170" y="515" width="560" height="180" rx="18" fill="#111c30" stroke="#ffbc66" stroke-width="2"/><text x="1190" y="549" class="h">L298N LOGIC 5 V — CONDITIONAL</text><path d="M1188 564 H1712" stroke="#ffbc66" stroke-width="2" opacity=".75"/><text x="1190" y="595" class="b">Only when module documentation calls for external logic 5 V</text><text x="1190" y="622" class="b">Disable onboard regulator as specified by 5V-EN instructions</text><text x="1190" y="649" class="b">Never connect two 5 V outputs together</text><path d="M400 260 H485 V250 H575" fill="none" stroke="#ffbc66" stroke-width="5"/><path d="M400 355 H475 V590 H575" fill="none" stroke="#c6ff59" stroke-width="5"/><text x="415" y="242" class="lab" fill="#ffbc66">MOTOR SUPPLY</text><text x="412" y="385" class="lab" fill="#c6ff59">BUCK INPUT</text><path d="M975 535 H1060 V210 H1170" fill="none" stroke="#c6ff59" stroke-width="5"/><path d="M1060 398 H1170" fill="none" stroke="#c6ff59" stroke-width="5"/><path d="M975 640 H1100 V605 H1170" fill="none" stroke="#c6ff59" stroke-width="4" stroke-dasharray="8 6"/><text x="1000" y="190" class="lab" fill="#c6ff59">REGULATED 5 V</text><rect x="70" y="745" width="1660" height="75" rx="16" fill="#1c2940" stroke="#b2c0d6" stroke-width="2"/><text x="100" y="776" class="h">COMMON GROUND — CONNECT GND BETWEEN BATTERY, L298N, BUCK, ESP32, SERVO</text><text x="100" y="802" class="s">Keep high motor current on its own battery wiring; do not route it through thin ESP32/servo ground wires.</text><rect x="70" y="850" width="1660" height="105" rx="18" fill="#301722" stroke="#ff657a" stroke-width="2"/><text x="100" y="888" class="h" fill="#ff657a">DO NOT</text><text x="225" y="888" class="b">Use the L298N 5 V output as the converter input, charge 3S from a single-cell charger, or tie two 5 V outputs together.</text><text x="100" y="923" class="b">Check your exact L298N 5V-EN jumper and ESP32 power path. Do not connect USB and external 5 V simultaneously unless verified safe.</text></svg>_Distribution.svg…]()


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

[Uploading SPARK_CA                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

Copyright 2026 SPARK Team

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and
 distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright
 owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities
 that control, are controlled by, or are under common control with that entity.
 For the purposes of this definition, "control" means (i) the power, direct or
 indirect, to cause the direction or management of such entity, whether by
 contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the
 outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions
 granted by this License.

"Source" form shall mean the preferred form for making modifications, including
 but not limited to software source code, documentation source, and configuration
 files.

"Object" form shall mean any form resulting from mechanical transformation or
 translation of a Source form, including but not limited to compiled object code,
 generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made
 available under the License, as indicated by a copyright notice that is included
 in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that
 is based on (or derived from) the Work and for which the editorial revisions,
 annotations, elaborations, or other modifications represent, as a whole, an
 original work of authorship. For the purposes of this License, Derivative Works
 shall not include works that remain separable from, or merely link (or bind by
 name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version
 of the Work and any modifications or additions to that Work or Derivative Works
 thereof, that is intentionally submitted to Licensor for inclusion in the Work
 by the copyright owner or by an individual or Legal Entity authorized to submit
 on behalf of the copyright owner. For the purposes of this definition,
 "submitted" means any form of electronic, verbal, or written communication sent
 to the Licensor or its representatives, including but not limited to communication
 on electronic mailing lists, source code control systems, and issue tracking
 systems that are managed by, or on behalf of, the Licensor for the purpose of
 discussing and improving the Work, but excluding communication that is
 conspicuously marked or otherwise designated in writing by the copyright owner
 as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of
 whom a Contribution has been received by Licensor and subsequently incorporated
 within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this
 License, each Contributor hereby grants to You a perpetual, worldwide,
 non-exclusive, no-charge, royalty-free, irrevocable copyright license to
 reproduce, prepare Derivative Works of, publicly display, publicly perform,
 sublicense, and distribute the Work and such Derivative Works in Source or
 Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License,
 each Contributor hereby grants to You a perpetual, worldwide, non-exclusive,
 no-charge, royalty-free, irrevocable (except as stated in this section) patent
 license to make, have made, use, offer to sell, sell, import, and otherwise
 transfer the Work, where such license applies only to those patent claims
 licensable by such Contributor that are necessarily infringed by their
 Contribution(s) alone or by combination of their Contribution(s) with the Work
 to which such Contribution(s) was submitted. If You institute patent litigation
 against any entity (including a cross-claim or counterclaim in a lawsuit)
 alleging that the Work or a Contribution incorporated within the Work
 constitutes direct or contributory patent infringement, then any patent licenses
 granted to You under this License for that Work shall terminate as of the date
 such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or
 Derivative Works thereof in any medium, with or without modifications, and in
 Source or Object form, provided that You meet the following conditions:

   (a) You must give any other recipients of the Work or Derivative Works a copy
       of this License; and

   (b) You must cause any modified files to carry prominent notices stating that
       You changed the files; and

   (c) You must retain, in the Source form of any Derivative Works that You
       distribute, all copyright, patent, trademark, and attribution notices
       from the Source form of the Work, excluding those notices that do not
       pertain to any part of the Derivative Works; and

   (d) If the Work includes a "NOTICE" text file as part of its distribution,
       then any Derivative Works that You distribute must include a readable
       copy of the attribution notices contained within such NOTICE file,
       excluding those notices that do not pertain to any part of the Derivative
       Works, in at least one of the following places: within a NOTICE text file
       distributed as part of the Derivative Works; within the Source form or
       documentation, if provided along with the Derivative Works; or, within a
       display generated by the Derivative Works, if and wherever such third-party
       notices normally appear. The contents of the NOTICE file are for
       informational purposes only and do not modify the License. You may add
       Your own attribution notices within Derivative Works that You distribute,
       alongside or as an addendum to the NOTICE text from the Work, provided
       that such additional attribution notices cannot be construed as modifying
       the License.

   You may add Your own copyright statement to Your modifications and may provide
   additional or different license terms and conditions for use, reproduction, or
   distribution of Your modifications, or for any such Derivative Works as a
   whole, provided Your use, reproduction, and distribution of the Work otherwise
   complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any
 Contribution intentionally submitted for inclusion in the Work by You to the
 Licensor shall be under the terms and conditions of this License, without any
 additional terms or conditions. Notwithstanding the above, nothing herein shall
 supersede or modify the terms of any separate license agreement you may have
 executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names,
 trademarks, service marks, or product names of the Licensor, except as required
 for reasonable and customary use in describing the origin of the Work and
 reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in
 writing, Licensor provides the Work (and each Contributor provides its
 Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied, including, without limitation, any warranties
 or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
 PARTICULAR PURPOSE. You are solely responsible for determining the
 appropriateness of using or redistributing the Work and assume any risks
 associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in
 tort (including negligence), contract, or otherwise, unless required by
 applicable law (such as deliberate and grossly negligent acts) or agreed to in
 writing, shall any Contributor be liable to You for damages, including any
 direct, indirect, special, incidental, or consequential damages of any character
 arising as a result of this License or out of the use or inability to use the
 Work (including but not limited to damages for loss of goodwill, work stoppage,
 computer failure or malfunction, or any and all other commercial damages or
 losses), even if such Contributor has been advised of the possibility of such
 damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or
 Derivative Works thereof, You may choose to offer, and charge a fee for,
 acceptance of support, warranty, indemnity, or other liability obligations
 and/or rights consistent with this License. However, in accepting such
 obligations, You may act only on Your own behalf and on Your sole
 responsibility, not on behalf of any other Contributor, and only if You agree
 to indemnify, defend, and hold each Contributor harmless for any liability
 incurred by, or claims asserted against, such Contributor by reason of your
 accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

   To apply the Apache License to your work, attach the following boilerplate
   notice, with the fields enclosed by brackets "[]" replaced with your own
   identifying information. (Don't include the brackets!) The text should be
   enclosed in the appropriate comment syntax for the file format. We also
   recommend that a file or class name and description of purpose be included
   on the same "printed page" as the copyright notice for easier identification
   within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
R_LICENSE_Apache_2.0.txt…]()

