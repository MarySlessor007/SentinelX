import re

from pathlib import Path


class LogParser:
    def __init__(self, logfile):
        self.logfile = Path(logfile)

    def read_logs(self):
        if not self.logfile.exists():
            raise FileNotFoundError(f"{self.logfile} not found.")

        with self.logfile.open("r") as file:
            return file.readlines()
        
    def parse_logs(self):
        parsed_logs = []

        pattern = re.compile(
            r'(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+).*?'
            r'(?P<status>Failed|Accepted)\s+password\s+for\s+'
            r'(?P<user>\w+)\s+from\s+'
            r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
        )

        for line in self.read_logs():
            match = pattern.search(line)

            if match:
                parsed_logs.append(match.groupdict())

        return parsed_logs
    