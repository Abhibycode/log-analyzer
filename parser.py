import re
import json
from datetime import datetime

class LogParser:
    def __init__(self, pattern_file="patterns.json"):
        with open(pattern_file, "r") as f:
            self.patterns = json.load(f)["patterns"]

    def detect_category(self, line):
        line_lower = line.lower()
        for category, keywords in self.patterns.items():
            if any(k in line_lower for k in keywords):
                return category
        return "OTHER"

    def extract_timestamp(self, line):
        timestamp_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
        return timestamp_match.group(0) if timestamp_match else None

    def parse_line(self, line):
        return {
            "timestamp": self.extract_timestamp(line),
            "category": self.detect_category(line),
            "raw": line.strip()
        }
