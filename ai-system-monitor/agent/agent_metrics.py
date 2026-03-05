import psutil
import requests
import socket
import time

URL = "http://127.0.0.1:8000/metrics"


while True:

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    network = psutil.net_io_counters().bytes_sent
    process_count = len(psutil.pids())

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    timestamp = time.time()

    data = {
        "cpu": cpu,
        "ram": ram,
        "network": network,
        "process_count": process_count,
        "ip": ip,
        "timestamp": timestamp
    }

    try:
        response = requests.post(URL, json=data)

        print("Sent:", data)
        print("Status:", response.status_code)
        print("Response:", response.text)

    except Exception as e:
        print("Error:", e)

    time.sleep(5)