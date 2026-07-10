from parser.log_parser import LogParser
from engine.detection_engine import DetectionEngine


def main():

    parser = LogParser(
        "sample_logs/auth.log"
    )

    logs = parser.parse_logs()


    engine = DetectionEngine()


    alerts = engine.detect_brute_force(logs)


    print("\nSecurity Alerts\n")


    for alert in alerts:
        print(alert)



if __name__ == "__main__":
    main()