# Day 07 – Design Thinking Before Coding

## Project: Log Analyzer CLI Tool

---

## What problem am I solving?

Applications and servers generate large log files every day.
Manually checking logs to understand system behavior takes a lot of time and can lead to mistakes.

This script automates log analysis by counting different types of log messages so a DevOps engineer can quickly understand system health.

The main goal is to:

- Quickly identify errors
- Monitor warnings
- Understand general application activity

---

## What input does my script need?

The script accepts input through command-line arguments.

### Required Inputs

- **Log File (`--file`)**
  - Path to the log file that needs analysis.
  - Example: `app.log`

- **Output File (`--out`)**
  - Path where the summary result will be saved.
  - Example: `summary.txt`

### Optional Input

- **Log Level Filter (`--level`)**
  - Filters logs by a specific level.
  - Supported values:
    - ERROR
    - WARNING
    - INFO

User provides:

- Log file location
- Output file location
- Optional log filtering level

---

## What output should my script give?

The script generates two types of output.

### 1.Terminal Output

A summary showing the count of each log level.

Example:

```text
Log Summary
INFO: 10
WARNING: 2
ERROR: 3
```

### 2.Output File

A text file containing the same summary results.

Example content:

```text
INFO: 10
WARNING: 2
ERROR: 3
```

---

## What are the main steps?

High-level workflow of the script:

1. User runs the CLI command with required arguments.
2. Script verifies whether the log file exists.
3. The log file is opened and read line by line.
4. Each log entry is analyzed.
5. Script detects log levels:
   - ERROR
   - WARNING
   - INFO
6. Counts occurrences of each log type.
7. Applies filtering if a log level is provided.
8. Displays the summary in the terminal.
9. Writes the summary to the output file.

---

## Why is this useful in DevOps?

- Helps quickly analyze production logs
- Speeds up debugging and troubleshooting
- Reduces manual monitoring effort
- Can be integrated into automation pipelines
- Improves operational visibility

---

## DevOps Mindset Learned

Before writing automation code, it is important to clearly understand:

- What problem is being solved?
- What input will the user provide?
- What output should be generated?
- What logical steps are required?

Planning first helps build reliable and production-ready automation.
