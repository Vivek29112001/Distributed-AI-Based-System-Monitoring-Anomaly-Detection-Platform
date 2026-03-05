import psutil
import socket
import time
import csv
import requests


API_URL = "http://127.0.0.1:8000/metrics"

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    process_count = len(psutil.pids())
    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    
    data = {
        "cpu": cpu,
        "ram": ram,
        "network": net,
        "process_count": process_count,
        "ip":ip,
        "timestamp": time.time()
    }
    
    return data
    
while True:
    metrics = collect_metrics()
    
    try:
        res = requests.post(API_URL, json=metrics)
        print("Sent: ", metrics)
        print("Response: ", res.json())
        
    except Exception as e:
        print("Error: ",e)
        
    time.sleep(5)
