import sys
import tempfile
import unittest

from pathlib import Path

# Allow imports from the project's src directory.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from log_analyser import analyse_logs, detect_suspicious_activity


class TestLogAnalyser(unittest.TestCase):

    def test_detects_suspicious_ip(self):
        failed_attempts = {
            "203.0.113.50": 10,
            "192.0.2.10": 1
        }

        alerts = detect_suspicious_activity(failed_attempts, threshold=5)

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["ip_address"], "203.0.113.50")

    def test_no_alert_below_threshold(self):
        failed_attempts = {
            "192.0.2.10": 2
        }

        alerts = detect_suspicious_activity(failed_attempts, threshold=5)

        self.assertEqual(len(alerts), 0)

    def test_alert_at_exact_threshold(self):
        failed_attempts = {
            "198.51.100.25": 5
        }

        alerts = detect_suspicious_activity(failed_attempts, threshold=5)

        self.assertEqual(len(alerts), 1)

    def test_empty_log(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "empty.log"
            log_file.write_text("", encoding="utf-8")

            results = analyse_logs(log_file)

            self.assertEqual(results["total_events"], 0)
            self.assertEqual(results["total_failed"], 0)
            self.assertEqual(results["total_successful"], 0)

    def test_successful_login_only(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "success.log"

            log_file.write_text(
                "Nov 02 09:00:01 server sshd[1001]: "
                "Accepted password for alice from "
                "192.0.2.10 port 51001 ssh2\n",
                encoding="utf-8"
            )

            results = analyse_logs(log_file)

            self.assertEqual(results["total_events"], 1)
            self.assertEqual(results["total_failed"], 0)
            self.assertEqual(results["total_successful"], 1)


if __name__ == "__main__":
    unittest.main()
