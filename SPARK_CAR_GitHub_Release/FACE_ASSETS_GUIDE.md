# Face Assets, Motion, Voice, and Sound Guide

All robot characters are original inline SVG/CSS drawings embedded in the dashboard. No profile photographs, remote image requests, or prerecorded video files are required. The 20 entries in Avatar Lab belong to the **main visual face library**. The independent floating companion system has exactly two character profiles: **PICO** and **BEEP**.

## Main avatar library

Selecting an item in the main Avatar Lab changes the large illustration and preview metadata. It does not change the character selected in the floating companion.

## PICO — curious penguin pal

PICO is curious, affectionate, clumsy, playful, a little noisy, and sleepy. On page entry he starts asleep, then performs one wake-and-approach animation, wobbles closer, nearly trips, catches himself, and greets the visitor. During use he may peek as the page scrolls, follow pointer movement, run in place, try to sing, whistle, giggle in beeps, play, become grumpy, or get sleepy. With longer inactivity he progresses through bored, sleepy, and sleeping.

## BEEP — calm signal comedian

BEEP is smart, witty, and usually calm. He has dialogue about signals, packets, Wi-Fi, diagnostics, and computer jokes. A randomized piano story starts with a good, confident mini-melody; then it deliberately goes wrong and BEEP becomes embarrassed and hides his face.

## Voice and sound

- **VOICE: ON/OFF** controls optional spoken lines through the browser Speech Synthesis API. PICO uses a higher pitch and quicker rate; BEEP uses a lower pitch and calmer pace. The exact voice is picked from available browser/OS voices and differs from device to device.
- **SOUNDS: ON/OFF** controls locally synthesized Web Audio effects: chirps, whistles, giggle-like beeps, grumbles, wake tones, sleepy sounds, and piano-like sequences. It is enabled by default in this edition where browser audio can run; autoplay restrictions may delay audible output until the first click.
- **TALK TO ME** speaks a short character line when voice support is available.
- **SIGNATURE SOUND** plays the selected character's signature effects.
- **HEAR THE TEAM INTRO** speaks the project, university, college, department, and team member names through the selected character voice, accompanied by a signature beep.

The project itself does not call a cloud voice API. Actual TTS voice provider and quality depend on the browser and OS configuration. Effects are generated in code; they are not recorded animal or human sounds.

## Facial expressions and movement

SVG overlays provide eyelids, eyebrow anger, blush, surprise, a whistle mouth, tears, heart eyes, music notes, and face-covering hands. CSS animation adds blinking, bouncing, clumsy wobble, singing, small running/zoomies, piano movement, and the entrance approach. These are procedural web animations, not video clips.

## Autonomy and safety

The large entry wake animation plays once per page load. The floating panel can be opened/closed without replaying it. Later interaction can gently wake a character from idle sleep but does not replay the entrance sequence. Random autonomous behavior runs in the browser only and does not generate requests to the ESP32 or trigger motor output. Reactions reflect the interface/controller state; the robot has no camera or motion sensor for these expressions. Hidden tabs throttle JavaScript timers, so idle timings are approximate.

Keep using the physical emergency disconnect when testing the real vehicle. Browser sounds are separate from the hardware buzzer connected to the ESP32.
