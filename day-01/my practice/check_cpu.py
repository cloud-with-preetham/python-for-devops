import psutil  # import package from pypi

# Aapko kaam karna hai ki user se CPU threshold lo
# Current CPU usage pata karo
# agar cpu usage threshold se zyada hua, email kar do


def check_cpu_limit():
    threshold = int(input("Enter the CPU threshold limit: "))

    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU %:", current_cpu)
    if current_cpu > threshold:
        print("CPU Alert Email sent...!")
    else:
        print("CPU is in safe state")


check_cpu_limit()
