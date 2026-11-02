# SOC Security Monitoring & Incident Investigation Lab

## Overview

A beginner-friendly cybersecurity homelab demonstrating SSH
authentication log analysis, suspicious activity detection,
Python automation and incident investigation.

The project uses simulated Linux authentication logs to
investigate repeated failed SSH login attempts and identify
potential password-guessing activity.

A Python-based log analyser automates the investigation
and generates alerts when an IP address exceeds a
configurable failed-login threshold.

**All authentication events are simulated. No real
systems were attacked or investigated.**

## Technologies

- Kali Linux
- Python 3
- Linux CLI
- SSH authentication log formats
- Regular expressions
- Python unittest
- Git and GitHub

## Project Structure

```text
soc-security-monitoring-lab/
├── README.md
├── logs/
│   └── simulated_auth.log
├── src/
│   └── log_analyser.py
├── tests/
│   └── test_log_analyser.py
├── docs/
│   └── investigation_notes.md
└── reports/
    └── incident_report.md
```

## How It Works

1. A synthetic SSH authentication log provides sample events.
2. The Python analyser reads the log file.
3. Failed and successful authentication events are identified.
4. Source IP addresses are extracted.
5. Failed login attempts are counted per IP address.
6. IP addresses meeting the alert threshold are flagged.
7. Investigation findings are documented in a SOC report.

## Running the Project

### Requirements

- Python 3
- Linux, macOS or Windows with Python installed
- No additional Python packages required

### Run the Log Analyser

From the project directory:

```bash
python3 src/log_analyser.py
```

### Expected Results

```text
Total Authentication Events: 20
Failed Login Attempts: 13
Successful Login Attempts: 7

Failed Attempts by IP:
203.0.113.50: 10
198.51.100.25: 2
192.0.2.10: 1

POTENTIAL SECURITY ALERTS:
[ALERT] 203.0.113.50 - 10 failed login attempts
```

## Detection Logic

The analyser uses a configurable threshold of five
failed authentication attempts per source IP.

If an IP address generates five or more failed attempts
across the analysed file, it is flagged for investigation.

This is a basic threshold-based detection rule.

An alert indicates potentially suspicious activity,
not confirmed malicious behaviour.

## Investigation Findings

The synthetic dataset contains:

- 20 authentication events.
- 13 failed authentication attempts.
- 7 successful authentication attempts.
- 10 failures from 203.0.113.50 within 45 seconds.
- Repeated attempts targeting admin and root.
- No observed successful authentication from the
  primary suspicious source.

A secondary source generated two failed logins
followed by a successful authentication.

The full investigation is available in:

`reports/incident_report.md`

## Automated Testing

Five automated tests validate:

1. Detection of an IP exceeding the threshold.
2. No alert below the threshold.
3. Alert generation at the exact threshold.
4. Handling an empty log file.
5. Handling a successful-login-only log.

Run the tests using:

```bash
python3 -m unittest discover -s tests -v
```

## Limitations

- Authentication logs are synthetic.
- The analyser processes an existing file rather
  than monitoring live events.
- Failed attempts are counted across the entire
  file rather than within a time window.
- The IP extraction pattern is designed for the
  sample IPv4 log format.
- No persistent database is used.
- No automated remediation or IP blocking occurs.
- Alerts do not establish that a compromise occurred.

## Future Improvements

- Add time-window-based detection.
- Support IPv6 authentication logs.
- Detect successful logins following repeated failures.
- Export alerts to JSON or CSV.
- Add real-time log monitoring.
- Integrate with a SIEM platform.
- Add more extensive automated tests.

## Skills Demonstrated

- Linux authentication log investigation
- Python scripting
- Security event analysis
- Threshold-based detection
- Regular expressions
- Automated testing
- Incident documentation
- Git version control

## Disclaimer

This project is intended for cybersecurity education
and portfolio development.

All events are fictional and use reserved
documentation IP address ranges.
