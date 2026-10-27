# Wiring and power guide

This guide documents the current code's signal mapping. Verify the exact ESP32-S2 Mini board revision and L298N module before making connections; clone-board pin labels and regulator jumpers can differ.

## Signal map

| ESP32-S2 GPIO | Destination | Configuration |
|---:|---|---|
| GPIO 7 | L298N IN1 | `MOTOR_IN1_PIN` |
| GPIO 6 | L298N IN2 | `MOTOR_IN2_PIN` |
| GPIO 4 | L298N IN3 | `MOTOR_IN3_PIN` |
| GPIO 5 | L298N IN4 | `MOTOR_IN4_PIN` |
| GPIO 11 | L298N ENA | `MOTOR_ENA_PIN`; verify ENA jumper arrangement |
| GPIO 12 | L298N ENB | `MOTOR_ENB_PIN`; verify ENB jumper arrangement |
| GPIO 13 | Servo signal | `BALL_SERVO_PIN` |
| GPIO 18 | Buzzer driver input | `BUZZER_PIN`; only if wired to buzzer circuit |

The physical RGB LED output code is removed. The status dot in the web page is drawn by the browser and does not require a board LED.

## 3S battery note

A conventional 3S LiPo pack is 11.1 V nominal and 12.6 V at full charge. It requires a compatible 3S balance charger. Do not use a single-cell power-bank/TP4056/IP5310 charger to charge a 3S pack.

For the current build, a safer typical arrangement is:

1. Battery positive feeds the L298N motor power input and the input of a suitable buck converter in parallel.
2. Battery negative connects to L298N GND and buck-converter input GND.
3. Adjust the buck output to **5.00 V with a multimeter before connecting electronics**.
4. Use the regulated output for the ESP32 board's documented 5 V/VBUS input and servo supply, if the board and servo ratings support it.
5. Join ESP32 GND, servo GND, buck GND, and L298N GND together.
6. Keep high motor current out of the ESP32's thin power/ground wiring.
7. Do not connect the buck converter's 5 V output to the L298N's 5 V terminal while the L298N regulator is enabled. Check the exact module's `5V-EN`/regulator jumper documentation before externally powering logic.
8. Avoid connecting USB and an external 5 V source simultaneously unless the exact ESP32 board's power-path behavior has been verified.

Do not assume the L298N's onboard 5 V regulator can supply the ESP32 and servo together. Its capacity and thermal margin depend on the exact module and the motor supply voltage.

## Motor/servo caution

- Use a motor supply compatible with the motors and L298N module.
- Size the servo supply for peak/stall current, not only idle current.
- A servo's red wire is normally its positive supply and brown/black is ground; verify your servo's datasheet.
- Never power a servo or motor from an ESP32 GPIO or from the 3V3 pin.
- Use a physical battery disconnect and inspect polarity before applying power.
- Initial motion test: lift the wheels off the desk, use a charged battery, and be ready to disconnect power.

## Buzzer

The code generates a two-tone sequence on GPIO 18 by default. A standard L298N module normally has no onboard buzzer. Only connect this output to an identified buzzer/signal input or a suitable transistor driver. Never drive a buzzer that exceeds GPIO current limits directly from the ESP32 pin.
