from collections import Counter
from pathlib import Path
import re

LOG_FILE = Path(__file__).resolve().parent.parent / "logs" / "simulated_auth.log"

ALERT_THRESHOLD = 5

def analyse_logs(log_file):
    failed_attempts = Counter()
    successful_attempts = Counter()

    total_events = 0
    total_failed = 0
    total_successful = 0

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:

            if "Failed password" in line:
                total_events += 1
                total_failed += 1

                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                if match:
                    ip_address = match.group(1)
                    failed_attempts[ip_address] += 1

            elif "Accepted password" in line:
                total_events += 1
                total_successful += 1

                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                if match:
                    ip_address = match.group(1)
                    successful_attempts[ip_address] += 1

    return {
        "total_events": total_events,
        "total_failed": total_failed,
        "total_successful": total_successful,
        "failed_attempts": failed_attempts,
        "successful_attempts": successful_attempts,
    }


def detect_suspicious_activity(failed_attempts, threshold=5):
    alerts = []

    for ip_address, count in failed_attempts.items():

        if count >= threshold:
            alerts.append({
                "ip_address": ip_address,
                "failed_attempts": count
            })

    return alerts


def display_results(results, alerts):

    print("=" * 40)
    print("       SOC SECURITY LOG ANALYSER")
    print("=" * 40)

    print(f"\nTotal Authentication Events: {results['total_events']}")
    print(f"Failed Login Attempts: {results['total_failed']}")
    print(f"Successful Login Attempts: {results['total_successful']}")

    print("\nFailed Attempts by IP:")

    for ip_address, count in results["failed_attempts"].most_common():
        print(f"{ip_address}: {count}")

    print("\nPOTENTIAL SECURITY ALERTS:")

    if alerts:
        for alert in alerts:
            print(
                f"[ALERT] {alert['ip_address']} - "
                f"{alert['failed_attempts']} failed login attempts"
            )
    else:
        print("No IP addresses exceeded the alert threshold.")

    print("\nAnalysis Complete.")



if __name__ == "__main__":

    results = analyse_logs(LOG_FILE)

    alerts = detect_suspicious_activity(
        results["failed_attempts"],
        ALERT_THRESHOLD
    )

    display_results(results, alerts)
