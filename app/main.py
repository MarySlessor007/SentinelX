from parser.log_parser import LogParser
from engine.detection_engine import DetectionEngine
from database.database import AlertDatabase


def main():

    parser = LogParser(
        "sample_logs/auth.log"
    )

    logs = parser.parse_logs()


    engine = DetectionEngine()

    alerts = engine.detect_brute_force(logs)


    database = AlertDatabase()


    for alert in alerts:

        database.insert_alert(alert)


    print("\nStored Alerts\n")

    for alert in database.get_alerts():

        print(alert)


if __name__ == "__main__":
    main()