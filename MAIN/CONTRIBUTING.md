# Contributing

Thanks for helping improve SPARK CAR. Focused bug reports, documentation fixes, UI refinements, and firmware improvements are welcome.

## Before opening a change

1. Describe the problem or improvement and the expected behavior.
2. Keep changes focused. Avoid mixing UI redesigns with motor pin changes unless necessary.
3. Do not add personal photographs or third-party assets without permission and attribution.
4. Never commit Wi-Fi passwords intended for deployment, tokens, private keys, or other secrets.
5. If a GPIO or timing value changes, update `config.h`, the README pin map, `WIRING.md`, and comments together.
6. If the page changes, update both `CyberCar_SPARK_CAR/index_preview.html` and the matching `PAGE_HTML` in `captive_portal.h`.

## Validation

Run:

```bash
python scripts/validate_project.py
```

If changing C++ or library use, also compile with your Arduino-ESP32 board package and `ESP32Servo`. Include the board/core version and any compiler output in your pull request. Hardware behavior should be tested with drive wheels raised before any floor test.

## Pull request checklist

- [ ] I described what changed and why.
- [ ] I updated documentation and pin maps where needed.
- [ ] The standalone HTML matches the embedded dashboard.
- [ ] Static validation passes.
- [ ] Any physical test is described honestly, including the board/core version.
- [ ] No secrets or unlicensed assets were added.
