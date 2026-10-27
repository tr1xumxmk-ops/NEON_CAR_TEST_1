# Firmware header guide

All headers are intended to stay next to `CyberCar_SPARK_CAR.ino` in the same Arduino sketch folder.

| File | Responsibility |
|---|---|
| `config.h` | Central compile-time settings: AP SSID/password, GPIO map, drive/servo timing, request intervals and safety timeout |
| `control_types.h` | Enumerations for drive commands, speed levels and operating modes; elapsed-time helper |
| `motor_driver.h` | L298N digital direction/enable logic, direction changes, drive profiles and motor output state |
| `accessories.h` | Servo wrapper and non-blocking buzzer pattern generator |
| `car_controller.h` | Integrates motor, servo, buzzer, manual timeout, emergency stop, AUTO demo and Q-learning UI mode behavior |
| `secure_backend.h` | Response security headers, JSON output, bounded integer parsing, Origin check and simple rate limiting |
| `captive_portal.h` | Captive portal helpers and complete inline dashboard HTML in the `PAGE_HTML` raw string |
| `web_routes.h` | HTTP endpoint handlers for drive, state, speed, mode, servo, horn, brake, and resume |
| `build_opt.h` | Compiler definitions intended to limit WebServer request-line/header wait and parser sizes on supported Arduino-ESP32 versions |
| `index_preview.html` | Standalone local simulation of the same dashboard HTML; does not control hardware |

The standalone preview HTML is mirrored inside `captive_portal.h`. The validation script fails when the copies differ. If editing the UI, update both copies in the same change.
