#ifndef SPARK_CAR_ACCESSORIES_H
#define SPARK_CAR_ACCESSORIES_H

#include <Arduino.h>
#include <ESP32Servo.h>
#include <stdint.h>
#include "config.h"

// Accessory wrappers: ball servo and the configured existing buzzer output.
class BallServoController {
 public:
  void begin() {
    servo_.setPeriodHertz(50);
    attached_ = servo_.attach(SparkConfig::BALL_SERVO_PIN,
                              SparkConfig::SERVO_MIN_US,
                              SparkConfig::SERVO_MAX_US) >= 0;
    angle_ = SparkConfig::SERVO_START_ANGLE;
    if (attached_) servo_.write(angle_); // requested starting position: 0 degrees
  }
  bool setAngle(const int angle) {
    if (angle < 0 || angle > 180 || !attached_) return false;
    angle_ = static_cast<uint8_t>(angle);
    servo_.write(angle_);
    return true;
  }
  uint8_t angle() const { return angle_; }
  bool attached() const { return attached_; }
 private:
  Servo servo_;
  uint8_t angle_ = SparkConfig::SERVO_START_ANGLE;
  bool attached_ = false;
};

class SparkBuzzer {
 public:
  void begin() {
    pinMode(SparkConfig::BUZZER_PIN, OUTPUT);
    noTone(SparkConfig::BUZZER_PIN);
    digitalWrite(SparkConfig::BUZZER_PIN, LOW);
    active_ = false;
    stepCount_ = 0;
    stepIndex_ = 0;
  }

  // Short confirmation tone for mode/speed/brake feedback. Non-blocking: the
  // main web-server loop continues running while the tone plays.
  void beep(const uint16_t frequency, const uint16_t durationMs) {
    stepCount_ = 1;
    stepIndex_ = 0;
    steps_[0] = {frequency, durationMs};
    startPattern(millis());
  }

  // Distinctive two-tone horn/buzzer, also non-blocking.
  void playHorn() {
    steps_[0] = {1040, 95};
    steps_[1] = {0, 45};
    steps_[2] = {760, 165};
    stepCount_ = 3;
    stepIndex_ = 0;
    startPattern(millis());
  }

  void tick(const uint32_t now) {
    if (!active_ || static_cast<int32_t>(now - stepDeadline_) < 0) return;
    ++stepIndex_;
    if (stepIndex_ >= stepCount_) {
      noTone(SparkConfig::BUZZER_PIN);
      digitalWrite(SparkConfig::BUZZER_PIN, LOW);
      active_ = false;
      stepCount_ = 0;
      return;
    }
    startStep(now);
  }

 private:
  struct ToneStep {
    uint16_t frequency;
    uint16_t durationMs;
  };

  ToneStep steps_[3] = {{0, 0}, {0, 0}, {0, 0}};
  uint8_t stepCount_ = 0;
  uint8_t stepIndex_ = 0;
  uint32_t stepDeadline_ = 0;
  bool active_ = false;

  void startPattern(const uint32_t now) {
    noTone(SparkConfig::BUZZER_PIN);
    if (stepCount_ == 0) {
      active_ = false;
      digitalWrite(SparkConfig::BUZZER_PIN, LOW);
      return;
    }
    active_ = true;
    startStep(now);
  }

  void startStep(const uint32_t now) {
    const ToneStep step = steps_[stepIndex_];
    if (step.frequency == 0) {
      noTone(SparkConfig::BUZZER_PIN);
      digitalWrite(SparkConfig::BUZZER_PIN, LOW);
    } else {
      tone(SparkConfig::BUZZER_PIN, step.frequency);
    }
    stepDeadline_ = now + step.durationMs;
  }
};
#endif // SPARK_CAR_ACCESSORIES_H
