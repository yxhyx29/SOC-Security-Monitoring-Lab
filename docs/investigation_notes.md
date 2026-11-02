# SOC Investigation Notes

## Investigation Overview

This investigation examines 20 simulated SSH authentication
events recorded on 2 November 2026.

The objective is to identify potentially suspicious authentication
activity and determine whether successful access was observed.

## Authentication Summary

- Total authentication events: 20
- Failed authentication attempts: 13
- Successful authentication attempts: 7

## Source IP Analysis

| Source IP | Failed Attempts |
|-----------|-----------------|
| 203.0.113.50 | 10 |
| 198.51.100.25 | 2 |
| 192.0.2.10 | 1 |

## Primary Finding

Source IP 203.0.113.50 generated 10 failed SSH
authentication attempts between 09:10:00 and 09:10:45.

Targeted usernames:
- admin: 7 attempts
- root: 3 attempts

No successful authentication from this source was observed
in the available logs.

## Secondary Finding

Source IP 198.51.100.25 generated two failed login attempts
followed by a successful authentication for user charlie.

Further investigation would be required to determine
whether this represents legitimate user activity.

## Initial Assessment

The repeated failed authentication attempts from
203.0.113.50 are consistent with possible SSH
password-guessing activity.

The available evidence does not establish that the
source successfully compromised the system.

## Limitations

- All events are simulated.
- The dataset contains only 20 authentication records.
- No endpoint, firewall or network telemetry was examined.
- Source IP addresses are reserved documentation addresses.
