import psutil


def get_thresholds():
    cpu_threshold = float(input("Enter CPU usage threshold (%): "))
    memory_threshold = float(input("Enter Memory usage threshold (%): "))
    disk_threshold = float(input("Enter Disk usage threshold (%): "))
    return (cpu_threshold, memory_threshold, disk_threshold)


def check_cpu(threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"\nCPU Usage: {cpu_usage}%")
    if cpu_usage > threshold:
        print("CPU usage is above threshold...!")
    else:
        print("CPU usage is normal or within limit...!")


def check_memory(threshold):
    memory_usage = psutil.virtual_memory()
    print(f"Memory Usage: {memory_usage.percent}%")
    if memory_usage.percent > threshold:
        print("Memory usage is above threshold...!")
    else:
        print("Memory usage is normal or within limit...!")


def check_disk(threshold):
    disk_usage = psutil.disk_usage("/")
    print(f"Disk Usage: {disk_usage.percent}%")
    if disk_usage.percent > threshold:
        print("Disk usage is above threshold...!")
    else:
        print("Disk usage is normal or within limit...!")


def main():
    print("""SYSTEM HEALTH CHECK""")
    cpu_t, memory_t, disk_t = get_thresholds()

    check_cpu(cpu_t)
    check_memory(memory_t)
    check_disk(disk_t)


if __name__ == "__main__":
    main()
