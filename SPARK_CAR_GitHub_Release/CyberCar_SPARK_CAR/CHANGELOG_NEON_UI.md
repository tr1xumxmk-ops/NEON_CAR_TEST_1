# SPARK CAR — Professional UI and Robot Avatar Update

- Refined the existing neon interface into a more professional robotics operations console while preserving the cyan, magenta, violet, and lime accent palette.
- Added six original inline SVG robot avatars: ORBIT, NOVA, BYTE, ECHO, SENTINEL, and MISO. The face library is selectable, includes Random Face and Reset controls, and uses no images, remote fonts, or external services.
- Added subtle CSS eye-blink/idle animations with `prefers-reduced-motion` support.
- Redesigned the university context block and team profiles with role labels, technical profile glyphs, skill tags, and a structured project-dossier layout. Existing member names and role labels remain.
- Preserved motor and servo functionality, buzzer behavior, existing backend paths, and safety logic.
- Kept the dashboard's physical LED output removed; its connection indicator is on-screen only.
- Synchronized the complete HTML between `index_preview.html` and the `PAGE_HTML` raw string in `captive_portal.h`.
- Validation: JavaScript passes `node --check`; no duplicate HTML IDs were detected; six avatar options and four team cards are present; embedded HTML matches the preview exactly. Full Arduino-ESP32 compilation and hardware testing were not available here.
