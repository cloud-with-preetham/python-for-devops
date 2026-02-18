import psutil

# Take threshold values of CPU, disk and memory from user input.


def get_thresholds():
    cpu_threshold = float(input("Enter the CPU (%): "))
    memory_threshold = float(input("Enter the memory (%): "))
    disk_threshold = float(input("Enter the disk (%): "))
    return (cpu_threshold, disk_threshold, memory_threshold)


def cpu_info(threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"\nCurrent CPU usage is {cpu_usage}%")
    if cpu_usage > threshold:
        print("WARNING: CPU Usage is over threshold.")
    else:
        print("CPU is safe to use...!")


def memory_info(threshold):
    memory_usage = psutil.virtual_memory()
    print(f"Current memory usage is {memory_usage.percent}%")
    if memory_usage.percent > threshold:
        print("Alert: Memory is high")
    else:
        print("Safe to use...!")


def disk_info(threshold):
    disk_usage = psutil.disk_usage("/")
    print(f"Current disk usage is {disk_usage.percent}%")
    if disk_usage.percent > threshold:
        print("Disk usage is above limit...!")
    else:
        print("Safe to use..!")


def main():
    print("""SYSTEM HEALTH CHECK""")
    cpu_t, memory_t, disk_t = get_thresholds()

    cpu_info(cpu_t)
    memory_info(memory_t)
    disk_info(disk_t)


if __name__ == "__main__":
    main()
