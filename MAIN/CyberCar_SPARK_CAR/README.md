# Firmware sketch — SPARK CAR

This directory contains the Arduino IDE sketch and every header file required by it.

- **Main sketch:** `CyberCar_SPARK_CAR.ino`
- **Live embedded dashboard:** `captive_portal.h`
- **Standalone preview copy:** `index_preview.html`
- **Configuration and pin map:** `config.h`
- **HTTP routes:** `web_routes.h`
- **Request validation and response helpers:** `secure_backend.h`

For the full project overview, hardware/power notes, installation guide, endpoint reference, safety information, and GitHub Pages preview instructions, see the [repository README](../README.md).

Open `CyberCar_SPARK_CAR.ino` from this folder in Arduino IDE. Keep the `.ino`, all `.h` files, and `build_opt.h` in the same folder when compiling.


See [`COMPANION_VOICES_AND_PERSONALITIES.md`](COMPANION_VOICES_AND_PERSONALITIES.md) for PICO/BEEP voice controls, autonomous reactions, the piano story, and the spoken team introduction.


See [`COMPANION_VOICES_AND_PERSONALITIES.md`](COMPANION_VOICES_AND_PERSONALITIES.md) for PICO/BEEP voice controls, autonomous reactions, the piano story, and the spoken team introduction.


### Floating companion behavior (current)

Only PICO and BEEP are available in the floating companion selector. The separate main Avatar Lab retains 20 visual character options. PICO and BEEP can speak using browser speech synthesis and play generated cute sounds. See [`COMPANION_VOICES_AND_PERSONALITIES.md`](COMPANION_VOICES_AND_PERSONALITIES.md) for personality stories, sound/voice controls, and the spoken team intro.


See [COMPANION_CINEMATIC_STORIES.md](COMPANION_CINEMATIC_STORIES.md) for the animated PICO and BEEP story system.
