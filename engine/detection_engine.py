from collections import defaultdict


class DetectionEngine:

    def __init__(self, threshold=5):
        self.threshold = threshold


    def detect_brute_force(self, logs):

        failed_attempts = defaultdict(int)

        alerts = []


        for log in logs:

            if log["status"] == "Failed":
                failed_attempts[log["ip"]] += 1


        for ip, count in failed_attempts.items():

            if count >= self.threshold:

                alerts.append(
                    {
                        "type": "SSH Brute Force",
                        "source_ip": ip,
                        "attempts": count,
                        "severity": "HIGH",
                        "mitre_id": "T1110",
                        "mitre_name": "Brute Force",
                        "tactic": "Credential Access"
                    }
                )

        return alerts