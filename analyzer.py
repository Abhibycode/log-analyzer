import os
import json
from parser import LogParser
from collections import defaultdict

class LogAnalyzer:
    def __init__(self):
        self.parser = LogParser()
        self.summary = defaultdict(int)
        self.details = defaultdict(list)

    def analyze_file(self, file_path):
        print(f"\nAnalyzing: {file_path}")
        with open(file_path, "r") as f:
            for line in f:
                parsed = self.parser.parse_line(line)
                category = parsed["category"]
                self.summary[category] += 1
                self.details[category].append(parsed)

    def generate_report(self, output="report.json"):
        report_data = {
            "summary": dict(self.summary),
            "details": self._convert_details()
        }
        with open(output, "w") as f:
            json.dump(report_data, f, indent=4)
        print(f"\nReport generated: {output}")

    def _convert_details(self):
        return {k: v for k, v in self.details.items()}

if __name__ == "__main__":
    folder = "sample_logs"
    analyzer = LogAnalyzer()

    for filename in os.listdir(folder):
        if filename.endswith(".log"):
            analyzer.analyze_file(os.path.join(folder, filename))

    analyzer.generate_report()

