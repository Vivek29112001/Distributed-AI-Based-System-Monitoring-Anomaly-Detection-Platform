import psutil
import socket
import requests
import time


url = "http://127.0.0.1:8000/metrics"


def get_ip():

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return ip


while True:

    metrics = {

        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "network": psutil.net_io_counters().bytes_sent,
        "process_count": len(psutil.pids()),
        "ip": get_ip(),
        "hostname": socket.gethostname(),
        "timestamp": time.time()
    }

    try:

        response = requests.post(url, json=metrics)

        print("Sent:", metrics)

    except Exception as e:

        print("Error:", e)

    time.sleep(5)