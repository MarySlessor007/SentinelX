from parser.log_parser import LogParser


def main():
    parser = LogParser("sample_logs/auth.log")

    logs = parser.parse_logs()

    print("\nParsed Log Entries\n")

    for log in logs:
        print(log)


if __name__ == "__main__":
    main()