# SPARK CAR Web Preview

The `index.html` file is the interactive browser preview for the SPARK CAR captive portal. It simulates the vehicle dashboard and does not control physical motors. The floating companion selector has exactly two personalities, PICO and BEEP, with autonomous animations, optional speech synthesis, and synthesized browser sounds.

To publish the preview, configure GitHub Pages to serve from the repository's `/docs` directory.


### Audio improvement
The latest portal release raises generated music/effects volume, adds a compressor to control overlapping notes, and includes a companion volume slider (50–150%, default 120%). It does not change hardware buzzer volume. More PICO/BEEP idle dialogue and expressive animation states are included.
