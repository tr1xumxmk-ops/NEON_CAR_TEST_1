# Security policy

## Intended deployment

SPARK CAR is designed for a trusted operator on a private, local Wi-Fi access point. The dashboard uses plain HTTP and does not implement TLS, user accounts, cryptographic pairing, or Internet-grade authentication. Do not port-forward it, publish it through a public tunnel, or connect it to an untrusted network bridge.

The default sample AP password is `12345678`. Change `SparkConfig::AP_PASSWORD` in `CyberCar_SPARK_CAR/config.h` before deploying, demonstrating, or sharing a running robot. Do not rely on the sample password for access control.

## Reporting a concern

For a non-sensitive code issue, open a GitHub issue with a concise description and reproduction steps. For a potential security issue, contact the repository maintainer privately through the contact route associated with the GitHub account instead of publishing exploit details in a public issue.

Do not include passwords, personal data, or private network details in bug reports. This repository currently has no guarantee of a formal response SLA.
