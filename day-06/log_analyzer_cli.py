import os
import argparse
from collections import Counter


class LogAnalyzer:
    """Initilaization"""

    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = []

    """Making read log files"""

    def read_logs(self):
        with open(self.log_file, "r", encoding="utf-8") as file:
            self.logs = file.readlines()

    """Analyzing the logs"""

    def analyze(self, level=None):
        counts = Counter()

        for line in self.logs:
            if level and level not in line:
                continue

            if "ERROR" in line:
                counts["ERROR"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1
            elif "INFO" in line:
                counts["INFO"] += 1
            else:
                pass

        return counts


def main():
    """Adding CLI Tool feature"""
    parser = argparse.ArgumentParser(description="Log Analzer CLI Tool")

    parser.add_argument("--file", required=True, help="Path to log file")

    parser.add_argument("--out", required=True, help="Output summary file path")

    parser.add_argument(
        "--level", required=False, help="Filter log by level (ERROR, INFO, WARNING)"
    )

    args = parser.parse_args()
    if not os.path.exists(args.file):
        print("Error: Log file not found!")
        return

    analyzer = LogAnalyzer(args.file)
    analyzer.read_logs()
    summary = analyzer.analyze(args.level)

    print("\nLog Summary")
    for level, count in summary.items():
        print(f"{level}: {count}")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as file:
            for level, count in summary.items():
                file.write(f"{level}: {count}\n")

        print(f"\nSummary written to {args.out}")


if __name__ == "__main__":
    main()
