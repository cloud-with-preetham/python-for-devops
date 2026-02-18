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

    def analyze_logs(self):
        self.error_count = 0
        self.info_count = 0

        for line in self.logs:
            if "ERROR" in line:
                self.error_count += 1
            elif "INFO" in line:
                self.info_count += 1

    """Summarizing the logs"""

    def print_summary(self):
        print("\nLog Analysis Summary")
        print("----------------------")
        print(f"INFO messages : {self.info_count}")
        print(f"ERROR messages : {self.error_count}")


if __name__ == "__main__":
    analyzer = LogAnalyzer("app.log")

    analyzer.read_logs()
    analyzer.analyze_logs()
    analyzer.print_summary()
