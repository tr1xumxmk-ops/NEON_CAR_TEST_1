#!/usr/bin/env python3
"""Static integrity checks for SPARK CAR's embedded captive portal and preview."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKETCH = ROOT / "CyberCar_SPARK_CAR"
PREVIEW = SKETCH / "index_preview.html"
PORTAL = SKETCH / "captive_portal.h"
PAGES_PREVIEW = ROOT / "docs" / "SPARK_CAR_Neon_Preview.html"
PAGES_INDEX = ROOT / "docs" / "index.html"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        SKETCH / "CyberCar_SPARK_CAR.ino",
        SKETCH / "config.h",
        SKETCH / "motor_driver.h",
        SKETCH / "accessories.h",
        SKETCH / "car_controller.h",
        SKETCH / "secure_backend.h",
        SKETCH / "captive_portal.h",
        SKETCH / "web_routes.h",
        SKETCH / "build_opt.h",
        PREVIEW,
        PORTAL,
        PAGES_PREVIEW,
        PAGES_INDEX,
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        fail("required files are missing: " + ", ".join(missing))

    html = PREVIEW.read_text(encoding="utf-8")
    portal = PORTAL.read_text(encoding="utf-8")
    match = re.search(r'R"SPARKHTML\(\n(.*?)\n\)SPARKHTML";', portal, flags=re.S)
    if not match:
        fail("could not locate PAGE_HTML raw string in captive_portal.h")
    embedded = match.group(1)
    if embedded != html:
        fail("index_preview.html and PAGE_HTML in captive_portal.h are not byte-for-byte synchronized")
    if PAGES_PREVIEW.read_text(encoding="utf-8") != html:
        fail("docs/SPARK_CAR_Neon_Preview.html is not synchronized with the sketch preview")
    if PAGES_INDEX.read_text(encoding="utf-8") != html:
        fail("docs/index.html is not synchronized with the sketch preview")

    face_ids = re.findall(r'<button\b[^>]*\bdata-face-id="([^"]+)"', html)
    if len(face_ids) != 20 or len(set(face_ids)) != 20:
        fail(f"expected 20 unique face buttons; found {len(face_ids)} ({len(set(face_ids))} unique)")
    sounds = re.findall(r'<button\b[^>]*\bdata-sound="([^"]+)"', html)
    if len(sounds) != 8 or len(set(sounds)) != 8:
        fail(f"expected 8 unique sound buttons; found {len(sounds)} ({len(set(sounds))} unique)")
    if 'id="sparkMiniPal"' not in html or 'id="sparkMiniOrb"' not in html:
        fail("floating SPARK PAL markup is missing")
    for mini_mood in ("zoomies", "surprised", "peek-left", "peek-right", "curious", "whistle", "angry", "bored", "sleepy", "sleeping", "offline"):
        if f'data-mood="{mini_mood}"' not in html and f"{mini_mood}:{{label:" not in html and f"'{mini_mood}':{{label:" not in html:
            fail(f"floating SPARK PAL mood is missing: {mini_mood}")
    if "setInterval(()=>{" not in html or "miniPalAutoStateTimer" not in html:
        fail("floating companion autonomous personality timer is missing")
    if 'id="sparkMiniCharacterSelect"' not in html or "miniPalSetCharacter" not in html:
        fail("independent companion character selector is missing")
    profile_ids = re.findall(r"^  ([a-z]+):\{name:", html, flags=re.M)
    if set(profile_ids) != {'pico', 'beep'}:
        fail(f"expected exactly the PICO and BEEP companion profiles; found {sorted(set(profile_ids))}")
    if 'id="picoTeamIntroButton"' not in html or 'HEAR THE TEAM INTRO' not in html:
        fail("spoken team introduction control is missing")
    if 'speechSynthesis' not in html or 'SpeechSynthesisUtterance' not in html or 'id="sparkMiniVoiceToggle"' not in html:
        fail("PICO/BEEP browser voice controls are missing")
    if "select.replaceChildren();['pico','beep'].forEach(id=>{const p=miniPalProfiles[id]" not in html:
        fail("floating companion selector is not restricted to PICO and BEEP")
    if 'miniPalPianoStory' not in html or 'pico-hide-face' not in html:
        fail("BEEP piano story and embarrassed face reaction are missing")
    if "window.addEventListener('scroll'" not in html:
        fail("floating companion scroll reaction is missing")
    for name in ("HAIDER NATHER", "AHMED AMJED", "AYAT SAYED", "BARAA FADHEL"):
        if name not in html:
            fail(f"team member name missing from preview: {name}")
    for required_label in ("MAKE SOUND", "A LOOK AT THE FACES", "PLAY A SOUND", "DO SOMETHING CUTE", "SIGNATURE SOUND", "TALK TO ME", "HEAR THE TEAM INTRO", "VOICE: OFF"):
        if required_label not in html:
            fail(f"expected dashboard label is missing: {required_label}")

    scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
    if not scripts:
        fail("no inline JavaScript blocks were found in the preview")
    node = shutil.which("node")
    if node:
        with tempfile.TemporaryDirectory(prefix="spark-car-js-") as tmp:
            for index, script in enumerate(scripts):
                js_file = Path(tmp) / f"script-{index}.js"
                js_file.write_text(script, encoding="utf-8")
                result = subprocess.run([node, "--check", str(js_file)], capture_output=True, text=True)
                if result.returncode:
                    print(result.stdout, file=sys.stderr)
                    print(result.stderr, file=sys.stderr)
                    fail(f"JavaScript syntax check failed for inline script {index}")
    else:
        print("NOTE: Node.js was not found; JavaScript syntax checks were skipped.")

    print("SPARK CAR static validation passed")
    print(f"  Embedded HTML matches preview: yes ({len(html)} characters)")
    print(f"  Unique robot faces: {len(face_ids)}")
    print(f"  Unique sound controls: {len(sounds)}")
    print(f"  Inline JavaScript blocks: {len(scripts)}")
    print(f"  JavaScript syntax checked: {'yes' if node else 'skipped (Node.js unavailable)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
