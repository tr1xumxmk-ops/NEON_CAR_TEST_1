# SPARK CAR — PICO & BEEP Companion Guide

## Only two floating companions

The floating companion selector contains exactly PICO and BEEP. The separate Face Library still includes 20 original visual avatars for the main dashboard; it does not add additional floating personalities.

### PICO — curious penguin pal
PICO is cute, curious, affectionate, a little noisy, clumsy, playful, and sleepy. When the page opens, he starts asleep, then performs one visual arrival sequence: wakes, waddles closer, nearly trips, catches himself, and greets the visitor. While the page is used he can follow scroll/pointer movement, peek left or right, run in place, try to sing, whistle, giggle in electronic chirps, play, act grumpy, get embarrassed, become bored, and eventually fall asleep. The initial arrival sequence happens once per page load; opening and closing his panel does not replay it.

### BEEP — calm signal comedian
BEEP is clever, funny, and mostly calm. He comments on networks, packets, signal strength, software diagnostics, and programming. One randomized mini-story has him start a piano recital confidently with a pleasant melody. A moment later, he deliberately hits wrong notes; he becomes embarrassed, covers his face, and explains that it was experimental jazz.

## Voice and cute sounds

- **VOICE: ON/OFF** enables/disables optional spoken lines. PICO uses a higher pitch and quicker rate; BEEP uses a lower pitch and calmer rate. The exact voice comes from the browser/operating system's installed voices, so no particular vocal identity or realistic character voice can be guaranteed.
- **SOUNDS: ON/OFF** controls browser-generated electronic effects such as chirps, whistles, giggle patterns, grumbles, sleepy tones, wake tones, and piano-like note sequences. Sound is enabled by default, but browser autoplay policies may block it until the first user interaction.
- **TALK TO ME** speaks a line for the selected character when browser speech synthesis is available.
- **SIGNATURE SOUND** plays a companion-specific sound or piano-style attempt.
- **HEAR THE TEAM INTRO** introduces the project, university, department, and names using the selected voice, with a signature beep at the start/end.

All electronic sound effects are synthesized locally using the Web Audio API. Spoken voice uses the browser Speech Synthesis API; actual voice quality and availability vary by device. Nothing is downloaded and no network service is needed.

## Autonomous reaction model

The floating companion reacts to the initial page entry, controller direction changes, servo actions, scroll direction, and throttled pointer movement. When idle, it selects randomized personality events. As inactivity grows, it transitions to boredom, sleepiness, and sleeping, with occasional soft sleep sounds. A later interaction can wake the character with a small reaction; it does not replay the big arrival/approach animation. Browsers throttle timers in hidden tabs, so timing is approximate.

Random personality behavior runs in the browser and does not send motor requests. The character reacts to interface/controller state, not physical sensor feedback. Drive controls and safety timeout remain separate from companion animation.

## Spoken team introduction

> SPARK CAR is a student robotics project from Al-Iraqia University, College of Engineering, Department of Artificial Intelligence and Robotics Engineering. The team members are Haider Nather, Ahmed Amjed, Ayat Sayed, and Baraa Fadhel.

## Try it

Open `CyberCar_SPARK_CAR/index_preview.html` or the GitHub Pages preview in a current Chrome, Edge, or Firefox browser. Use **VOICE: ON** and **SOUNDS: ON**, then try **TALK TO ME**, **SIGNATURE SOUND**, and **HEAR THE TEAM INTRO**. If you hear nothing, check tab/device volume, ensure a browser voice is available, and click a sound button to unlock audio. GitHub's source-code view does not run the preview; use the standalone HTML file or GitHub Pages.

## Limitations and verification

These are programmed SVG/CSS expressions and synthesized sound effects, not prerecorded videos or real animal recordings. The Web Audio / speech behaviors depend on browser support. The HTML preview simulates car state; physical motor/servo control requires the ESP32-hosted portal. Compile and test the firmware on the target board before deployment.


## Cinematic stories and reactions

For the exact wake-up sequence, PICO singing story, BEEP piano fail story, browser voice restrictions, and scroll-interruption behavior, see [Cinematic PICO & BEEP Companion Stories](COMPANION_CINEMATIC_STORIES.md) in this firmware folder or [the repository guide](PICO_BEEP_CINEMATIC_BEHAVIOUR.md) at the root.


## Cinematic stories and reactions

For the exact wake-up sequence, PICO singing story, BEEP piano fail story, browser voice restrictions, and scroll-interruption behavior, see [Cinematic PICO & BEEP Companion Stories](COMPANION_CINEMATIC_STORIES.md) in this firmware folder or [the repository guide](PICO_BEEP_CINEMATIC_BEHAVIOUR.md) at the root.
