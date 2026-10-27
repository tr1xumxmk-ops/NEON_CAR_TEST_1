# Local backend and request-hardening notes

## Trust boundary

The firmware starts a Wi-Fi access point and a plain-HTTP web server on the ESP32. It is designed for direct, local control while a trusted operator is connected to the robot's AP. It is not an Internet service and must not be port-forwarded or exposed through a public proxy.

The example AP credentials live in `CyberCar_SPARK_CAR/config.h`. The current demo password is well-known and must be changed before a public demonstration. Source control is not a secure secret store; do not commit real credentials.

## Input handling

- Drive directions are matched against a fixed allowlist: `forward`, `backward`, `left`, `right`, `stop`.
- Speed levels and operating modes are matched against fixed allowlists.
- Servo angle is parsed as an integer and bounded to 0–180.
- State-changing routes check the `Origin` header against the expected local portal origin.
- Selected endpoint classes use request cooldowns. Identical drive refreshes are coalesced, while genuine direction changes and stop requests receive priority.
- Responses are JSON and carry conservative browser security headers.
- No incoming input is evaluated as JavaScript or C++ code.

The API request bodies are form-encoded by the browser; JSON is used for server responses/state. This distinction is intentional in the current implementation.

## Remaining limitations

- Plain HTTP has no transport encryption. Anyone with access to the local Wi-Fi may observe traffic.
- Origin checking is not user authentication and can be spoofed by non-browser clients. Treat the Wi-Fi AP password as the local access gate, and use a strong, unique password.
- The network does not implement per-user accounts, a secure pairing flow, TLS, or remote/cloud authorization.
- Browser captive mini-windows and OS network behavior are outside the firmware's control.
- A compromised device connected to the access point may be able to issue control requests.

Keep the AP isolated; do not port-forward the dashboard or connect it to an untrusted bridge. A physical power disconnect remains necessary for safe operation.
