# SOC Security Investigation Report

## 1. Investigation Details

**Investigation ID:** SOC-LAB-001

**Investigation Date:** 2 November 2026

**Environment:** Simulated Linux SSH authentication logs

**Investigation Type:** Suspicious authentication activity

**Status:** Investigation completed - simulated environment

**Priority:** Medium (illustrative assessment)

---

## 2. Executive Summary

An investigation was conducted into 20 simulated SSH
authentication events recorded on a Linux server.

Analysis identified 13 failed authentication attempts
and 7 successful authentication attempts.

The primary finding involved source IP address
203.0.113.50, which generated 10 failed authentication
attempts within 45 seconds.

The activity targeted the administrative usernames
admin and root.

This behaviour is consistent with possible SSH
password-guessing activity.

No successful authentication from this source was
observed within the available dataset.

All events and IP addresses used in this investigation
are synthetic.

---

## 3. Investigation Objectives

The investigation aimed to:

- Identify failed and successful SSH authentication attempts.
- Determine which source IP addresses generated failures.
- Identify potentially suspicious authentication patterns.
- Investigate whether successful access was observed.
- Document findings and recommend security improvements.

---

## 4. Evidence Summary

### 4.1 Authentication Statistics

| Metric | Result |
|--------|--------|
| Total authentication events | 20 |
| Failed authentication attempts | 13 |
| Successful authentication attempts | 7 |
| Unique IPs generating failures | 3 |

### 4.2 Failed Attempts by Source

| Source IP | Failed Attempts |
|-----------|-----------------|
| 203.0.113.50 | 10 |
| 198.51.100.25 | 2 |
| 192.0.2.10 | 1 |

### 4.3 Targeted Accounts

Source IP 203.0.113.50 targeted:

- admin: 7 failed attempts
- root: 3 failed attempts

The attempts occurred between 09:10:00 and 09:10:45
on 2 November 2026.

---

## 5. Technical Analysis

The investigation used Linux command-line tools,
including grep, awk, sort and uniq, to examine
authentication records.

A Python-based log analyser was also developed
to automate the identification of failed login
attempts and source IP addresses.

The analyser uses a configurable threshold of
five failed authentication attempts per IP address.

When an IP reaches or exceeds this threshold,
the program generates a potential security alert.

Source IP 203.0.113.50 exceeded this threshold
with 10 failed authentication attempts.

This activity is consistent with a possible
SSH password-guessing attempt.

However, the available logs do not establish
malicious intent or successful compromise.

---

## 6. Secondary Finding

Source IP 198.51.100.25 generated two failed
authentication attempts followed by a successful
login for user charlie.

This could represent legitimate user activity,
such as entering an incorrect password twice.

Additional authentication context would be
required to determine whether the activity
was suspicious.

---

## 7. Impact Assessment

No successful authentication from the primary
suspicious IP address was observed.

There is insufficient evidence to conclude
that the system was compromised.

The investigation demonstrates detection of
potentially suspicious authentication activity,
not confirmation of a security breach.

---

## 8. Recommendations

The following measures could reduce SSH
authentication risks:

1. Use SSH public-key authentication where appropriate.
2. Disable password-based SSH authentication when feasible.
3. Restrict SSH access using network controls.
4. Implement rate limiting or tools such as Fail2ban.
5. Enable centralised authentication logging and monitoring.
6. Investigate repeated authentication failures.
7. Review successful logins following unusual failures.
8. Apply least-privilege access controls.

---

## 9. Investigation Limitations

- All authentication events are simulated.
- The dataset contains only 20 records.
- IP addresses are reserved documentation addresses.
- No real SSH server was attacked or investigated.
- No endpoint or firewall telemetry was collected.
- The analyser uses a basic count-based detection rule.
- The detection rule does not currently use time windows.
- Logs are analysed offline rather than in real time.
- No automated blocking or remediation was implemented.

---

## 10. Conclusion

The investigation successfully identified a source
generating repeated failed SSH authentication attempts.

Linux command-line analysis and Python automation
produced consistent findings.

Five automated tests were completed successfully,
covering alert thresholds and basic log analysis.

The project demonstrates introductory SOC skills,
including log investigation, suspicious activity
detection, Python scripting, automated testing
and technical reporting.

No confirmed compromise was identified.

