import json
from datetime import datetime

LOG_FILE = "app.log"
OUTPUT_FILE = "log_summary.json"


def read_log_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("Log file is empty")
        return lines

    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        exit(1)

    except ValueError as err:
        print(f"{err}")
        exit(1)


def analyze_logs(lines):
    """Count INFO, WARNING AND ERRORS Messages"""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in lines:
        for level in counts:
            if level in level.upper():
                counts[level] += 1
    return counts


def print_summary(summary):
    """Print result to terminal"""
    print("\nLog Analysis Summary")
    print("-" * 30)

    for level, count in summary.items():
        print(f"{level:<10}: {count}")
    print("-" * 30)


def write_summary_to_file(summary, output_file):
    """Write summary to JSON file"""
    data = {"generated at": datetime.now().isoformat(), "summary": summary}

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"\nSummary  written to {output_file}")

    except Exception as err:
        print(f"Failed writing output file {err}")


def main():
    """Main execution flow"""
    log_lines = read_log_file(LOG_FILE)
    summary = analyze_logs(log_lines)
    print_summary(summary)
    write_summary_to_file(summary, OUTPUT_FILE)


if __name__ == "__main__":
    main()
