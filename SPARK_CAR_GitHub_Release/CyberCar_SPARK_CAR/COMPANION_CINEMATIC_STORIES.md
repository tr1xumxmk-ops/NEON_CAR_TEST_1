# Cinematic PICO & BEEP Companion Stories

This release turns the floating companion from a small badge into a sequence of choreographed mini-scenes. The scenes are composed live from inline SVG, CSS keyframes, timed browser audio, and optional browser speech. They are **video-like animations, not prerecorded MP4 files**. This keeps the ESP32 portal self-contained and offline-capable.

## The page-entry arrival

When the page loads, the selected companion starts asleep. The scene shows breathing motion and drifting `Z` marks, then the character opens their eyes, waddles toward the viewer, nearly trips, catches themself, and celebrates. The full arrival runs once per page load. Switching between PICO and BEEP starts a separate wake-up sequence for the newly selected character; opening or closing the companion's small control panel does not replay the page-entry animation.

The spoken welcome is queued until the user first interacts with the page if the browser blocks automatic audio. This is a browser security rule rather than an ESP32 bug.

## PICO: tiny concert, giant feelings

PICO's scene has a multi-act mini story: he introduces a song, plays a timed high-pitched melody while his face and music notes animate, forgets the ending, hits a comic wrong note, wobbles, and attempts a proud little bow. He can also randomly peek at scrolling, get curious, run in place, giggle, whistle, act grumpy, become bored, get sleepy, and sleep. His character is affectionate, curious, a little noisy, and deliberately clumsy.

## BEEP: the piano incident

BEEP announces a flawless performance, then plays a short melody. The little eight-key keyboard highlights each key as the corresponding Web Audio note plays. He grows overconfident, launches into a deliberately wrong and faster sequence, flashes the wrong keys, freezes, covers his face, and explains that it was “experimental jazz.” The story then gives him a chance to peek out and pretend to inspect diagnostics.

The good and bad parts are timed in sequence: the failure does not begin before the first melody has finished. This was important for making the scene feel like a little cartoon story instead of overlapping sound effects.

## Autonomous behavior and scrolling

- Idle events are selected randomly; a character may whistle, dance, make a tiny joke, sing, try the piano story, or act grumpy.
- After roughly 32 seconds without interaction the companion may show boredom; after roughly 58 seconds sleepiness; after roughly 83 seconds sleeping. Timing is approximate because browsers throttle background tabs.
- Scrolling triggers a throttled visual peek and does not send motor commands or reset the idle timer.
- If the user scrolls a meaningful distance while a companion is actively speaking, the current line/story is cancelled and the companion may react with a grumpy comment.
- Ordinary motor/servo moves no longer show repeated success pop-ups. Only actionable errors are shown. The companion's response to drive commands is a local visual effect, not an additional API request.

## Voices and cute synthesized audio

- **SOUNDS** controls Web Audio beeps, notes, whistles, grumbles and sleep sounds.
- **VOICE** controls spoken dialogue using the browser's Speech Synthesis API. PICO uses a higher/faster profile; BEEP a lower/slower profile. Actual voice availability and sound depend on browser and operating system. These are not custom-trained or recorded character actors.
- Browser audio generally requires a user gesture. Click the webpage once, then leave SOUNDS and VOICE enabled if you want their autonomous actions to be audible.
- The spoken team introduction includes SPARK CAR, Al-Iraqia University, College of Engineering, Artificial Intelligence & Robotics Engineering Department, and the four team names. It ends with a signature sound when audio effects are enabled.

## Physical control and safety

The companion runs in the browser. Random scenes and sounds do not make additional ESP32 requests. The motor control, servo API, configured hardware-buzzer endpoint, and firmware movement timeout stay separate. Face reactions represent the controller/requested state, not physical sensor feedback. Test with wheels raised and a physical battery disconnect accessible.

## Try it

Open `CyberCar_SPARK_CAR/index_preview.html` locally or use the hosted page after enabling GitHub Pages from `/docs`. Select BEEP, open the floating companion panel, and trigger the signature-story button to see the piano story; select PICO to trigger the singing story. Enable SOUNDS and VOICE with an initial user click to hear generated notes and optional speech.

## Audio volume and new idle acting (2026-10-27)

Browser-created notes now use a higher per-note level and a shared dynamics compressor to make music and beep reactions more audible while preventing excessive peaks when notes overlap. The floating companion panel includes a 50–150% browser-audio volume slider (default 120%). The slider affects generated Web Audio effects/music only; it does not change speech-synthesis volume, the ESP32 hardware horn, or motor outputs.

PICO's random idle pool now includes sneeze, dance, dizzy spin, eureka, blush, juggling, cozy/purr, waving, and obstacle-course jokes. BEEP's pool includes bug-fix celebrations, debugging loops, dance-algorithm jokes, technical blushes, pretend dust sneezes, juggling diagnostics, and more programming/network jokes. Matching CSS states add new movement patterns for these expressions.

Spoken random dialogue remains subject to the VOICE toggle, browser audio unlock requirements, and the availability of a suitable system voice. The companion sound toggle must be enabled for synthesized sound effects and music.
