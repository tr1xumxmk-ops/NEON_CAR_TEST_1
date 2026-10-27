# SPARK CAR — Cute Cartoon Stories & Extra Reactions

The floating companion now has more little animated stories in addition to its dance routines, singing scene, piano recital, wake-up sequence, and sleep behavior. These scenes are generated live using SVG artwork, CSS keyframes, timed captions, optional browser speech, and Web Audio beeps. They are not prerecorded videos and they do not call motor-control API routes.

## New PICO stories
- **The Elegant Walk / Banana Peel:** PICO waddles across the stage, slips, performs a tiny floor inspection, gets dizzy, recovers, and issues the banana peel a formal warning.
- **Pip-Choo:** PICO investigates a sparkle, builds up to a sneeze, launches imaginary glitter, and apologizes to the dust.
- **Imaginary Cookie:** PICO spots a cookie, zooms after it, pounces on empty air, and comforts himself with the idea of a snack.
- **Who Is That Shadow?:** PICO is suspicious of a shadow, realizes it is his own, and makes a new best friend.
- **Tiny Zoomies:** PICO runs a four-pixel race and requests a medal and a nap.
- **The Overly Graceful Bow:** PICO attempts a formal bow and nearly tips over.

## New BEEP stories
- **Runaway Packet:** BEEP chases a glowing packet, skids, catches it, and discovers it was his own notification.
- **Bug Detective:** BEEP investigates a one-pixel bug that jumps around and becomes the self-appointed project manager.
- **Calibrated Bow:** BEEP's carefully measured bow exceeds its angle limit and ends in an embarrassed recovery.
- **Coffee Interface Incident:** BEEP spills an imaginary cup and files a report on the incident.
- **Deep Diagnostics:** BEEP finds a confidence overflow and creates two new errors while fixing one.

## How to experience them
- Let the page remain visible: autonomous events randomly choose new stories and one-line dialogues while the companion is awake.
- Use **SURPRISE MINI-CARTOON** to trigger a random story immediately.
- Enable the companion's **SOUNDS** and **VOICE** controls for beeps and spoken dialogue. Browser autoplay policies may require a click/tap first.
- Scrolling can cause a peek reaction, but it does not reset the boredom timer. Idle timers may be throttled when the browser tab is hidden.

## Technical notes
- Stories are serialized: a new story will not start while another story is active.
- Each act updates the face mood, scene caption, prop, movement keyframes, and optional sound.
- Closing the story cancels its scene token so later acts should not continue changing the scene.
- All story behavior stays in the browser. It does not send extra drive/servo HTTP requests and does not alter firmware safety timeouts.
- Prefer reduced motion is respected by disabling the new continuous/strong motion animations.
