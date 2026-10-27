# Publishing this project on GitHub

This package is arranged as a repository root, with a README, firmware folder, docs preview, validation workflow, issue templates, and licenses.

## Option A — publish as a new repository

1. Extract the release ZIP into a clean folder.
2. Create an empty GitHub repository, for example `SPARK_CAR_Neon_Companion`. If creating a new repository, do not initialize it with another README/license because this package already contains them.
3. From the extracted folder, run:

   ```bash
   git init -b main
   git add .
   git status
   git commit -m "Prepare SPARK CAR Live Companion for GitHub"
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   git push -u origin main
   ```

4. Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with the actual GitHub values. Do not paste a personal access token into this document or commit it to the repository.
5. Check the repository Actions tab. The static validation workflow should run on the first push.
6. In **Settings → Pages**, choose deployment from a branch, select `main` and `/docs`, then save. GitHub Pages serves `docs/index.html`, a simulated UI preview only; it does not connect to the robot.
7. Add suggested topics: `esp32`, `esp32-s2`, `arduino`, `robotics`, `robot-car`, `captive-portal`, `embedded-systems`, `svg`, `web-audio`.

Suggested GitHub description:

> Offline-first ESP32-S2 robot car with neon captive-portal controls, 20 original vector robot avatars, servo and buzzer controls, and browser-generated sound effects.

## Option B — add it to the existing CyberCar repository

Your referenced repository already contains another CyberCar edition and hardware/PCB documentation. To preserve those files, do **not** blindly replace the old repository with this package. Copy `CyberCar_SPARK_CAR/` into the existing repository as a sibling project folder, then merge the relevant README links and shared `.github` files deliberately. Review any naming collisions, especially `README.md`, `LICENSE`, `NOTICE.md`, and existing workflow files, before committing.

## Before the first public release

- Change `SparkConfig::AP_PASSWORD` in `CyberCar_SPARK_CAR/config.h` from the sample `12345678` to a strong, unique password before flashing a publicly demonstrated robot.
- Verify that you have permission to publish the names/roles shown in the team section. The UI contains no team photographs.
- Confirm all GPIO connections against the actual board and L298N module.
- Compile with the Arduino-ESP32 3.x core and ESP32Servo library; static CI does not replace a real firmware build.
- Test with wheels raised, an adequately charged battery, a suitable regulated 5 V servo/ESP32 supply, common ground, and an accessible physical battery disconnect.
- Do not expose the local HTTP portal to the public Internet.
