# SPARK CAR — Face Library and Team UI

## Original robot avatars

The portal includes twenty offline-ready vector faces:

- **ORBIT** — welcoming navigator, cyan optics
- **NOVA** — curious explorer, angular magenta optics
- **BYTE** — pixel-inspired technician, lime optics
- **ECHO** — calm assistant, violet dome
- **SENTINEL** — focused guardian, warm orange optics
- **MISO** — playful companion, amber optics
- **PIP** — cute bean cheerleader, pink optics
- **BUBU** — sleepy cloud-bot, pale cyan optics
- **KIKI** — curious kitty-inspired explorer, amber optics
- **LUMI** — starry optimistic companion, violet optics
- **MOCHI** — marshmallow-like friend, pearl-violet optics
- **TOTO** — springy antenna bot, lime optics

Each avatar is hand-authored as inline SVG and can be selected in the browser. Selecting one updates both the library preview and the live companion above the driving controls. `RANDOM FACE` selects another avatar; `RESET` returns to ORBIT. The companion is a visual response to the controller state and does not issue motor or servo commands.

## Team presentation

The team section now uses abstract technical profile illustrations rather than photos. It includes role labels, focus descriptions, engineering-discipline tags, sequential project-role identifiers, and a clearly displayed university/department context. The cards are responsive and keep the project's existing member names.

## Files to edit

- `index_preview.html`: standalone browser preview with simulated API calls
- `captive_portal.h`: same HTML embedded for the ESP32 portal

These two HTML sources are intentionally synchronized. If you later edit the face designs or page layout, apply the same full HTML to both so the offline preview stays representative of the live portal.

## Live reaction system

The selected face is displayed in a companion panel above the driving controls. The face changes animation state for driving forward/backward/left/right, stopping, servo movement, horn, emergency brake, and connection loss. The CSS animations are short lightweight reactions rather than video assets. Optional cute whistle/chime audio is generated locally with the Web Audio API, defaults to OFF, and is enabled only by an explicit click.

- **PUDDLE** — soft rain-drop bot
- **NIBLET** — bunny-eared friend
- **SPROUT** — garden-inspired green bot
- **COMET** — starry space pal
- **WINK** — cheeky one-eyed bot
- **TOFU** — pearl-colored marshmallow bot
- **PICO** — penguin-inspired companion
- **BEEP** — antenna signal buddy

The Sound Lab provides whistle, boop, twinkle, happy, giggle-like chirps, bubble, sleepy, and magic patterns synthesized locally in the browser.
