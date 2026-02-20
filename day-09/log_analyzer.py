from collections import Counter


def analyze_logs(file_path):
    levels = []

    with open(file_path, "r") as file:
        for line in file:
            if "INFO" in line:
                levels.append("INFO")
            elif "WARN" in line:
                levels.append("WARN")
        return dict(Counter(levels))
