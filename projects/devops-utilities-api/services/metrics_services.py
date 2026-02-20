import psutil


def get_system_metrics():
    """
    This API gets the System Metrics(CPU, Memory & Disk Usage Percentage) of the system it is running on.
    Based on a CPU Threshold
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    cpu_threshold = 20
    cpu_status = "High" if cpu_percent > cpu_threshold else "Low"
    print(f"{cpu_status} CPU Usage: {cpu_percent}%")

    memory_threshold = 40
    memory_status = "High" if memory_percent > memory_threshold else "Low"
    print(f"{memory_status} Memory Usage: {memory_percent}%")

    disk_threshold = 50
    disk_status = "High" if disk_percent > disk_threshold else "Low"
    print(f"{disk_status} Disk Usage: {disk_percent}%")

    return {
        "cpu_percent": cpu_percent,
        "cpu_status": cpu_status,
        "memory_percent": memory_percent,
        "memory_status": memory_status,
        "disk_percent": disk_percent,
        "disk_status": disk_status,
    }
