# SPARK CAR — Hardware Bill of Materials (BOM)

This BOM describes the current prototype. Exact modules, board clones, servo models, motors and battery capacities may differ between builds; verify each part's datasheet and pin labels.

| Qty | Item | Function | Selection / safety notes |
|---:|---|---|---|
| 1 | ESP32-S2 Mini-compatible dev board | Wi-Fi access point and firmware | Check exact clone pinout, USB behavior and approved 5 V input path. GPIO is 3.3 V logic. |
| 1 | L298N dual H-bridge module | Two-motor drive | Verify current/thermal limits, motor-supply range, ENA/ENB jumpers and `5V-EN` regulator jumper. |
| 2 | DC gear motors | Drive wheels | Match rated voltage/current to L298N and battery. Stall current matters. |
| 1 | Chassis and wheel set | Mechanical platform | Ensure no cable is close to wheels, gears or servo arm. |
| 1 | Standard 3S LiPo pack (prototype configuration) | Main battery | 11.1 V nominal, 12.6 V full for typical 4.2 V/cell LiPo. Use compatible 3S balance charger and appropriate protection. |
| 1 | Regulated 5 V buck converter | ESP32 and servo/accessory supply | Input rating must exceed 12.6 V with margin. Continuous current must cover ESP32, servo stall/peak current and accessories; allow thermal margin. |
| 1 | Hobby servo compatible with regulated supply | Servo/ball mechanism | Signal currently on GPIO13. Verify supply voltage, stall current, connector polarity, travel and mechanical range. |
| 1 | Compatible buzzer / piezo / buzzer-driver circuit (optional) | Physical horn | Control signal GPIO18 by default. L298N normally has no built-in buzzer; never overdraw an ESP32 GPIO. |
| As needed | Wires, plugs, fuse, heat-shrink, mounting hardware | Safe interconnects | Use adequate wire gauge for motor/battery current and strain relief. Insulate all bare terminals. |
| 1 | Accessible battery disconnect or switch | Emergency electrical isolation | Must safely interrupt the battery/current for the build. Software stop is not isolation. |
| 1 | USB data cable | Flash/debug | Charge-only cables cannot upload firmware. |
| 1 | Digital multimeter | Bring-up and debugging | Verify battery polarity and set/measure the 5 V buck output before connecting electronics. |

## Optional tools

- Small screwdriver for converter adjustment and terminal blocks.
- Soldering tools and heat-shrink if required by the build.
- Current-limited bench supply for initial electronics tests, if available.
- Digital caliper or ruler for mechanical fit checks.

## Power design notes

- The 5 V buck converter is supplied from the battery pack in a separate branch from the motor-driver supply. Do not power a boost/buck module from the L298N's 5 V output.
- Set the converter to **5.00 V with a multimeter** before connecting it to the ESP32 or servo.
- Don't connect two 5 V outputs together. Review the exact L298N `5V-EN` arrangement if the external 5 V rail is also used for L298N logic.
- Do not use a TP4056/IP5310/single-cell power-bank charger on a 3S pack.
- Do not power DC motors or servo from the ESP32 GPIO or 3V3 pin.

See [WIRING.md](WIRING.md) for wiring diagrams and the full checklist.
