import psutil
import socket
import time
import csv

def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    process_count = len(psutil.pids())
    
    return {
        "cpu": cpu,
        "ram": ram,
        "network": net,
        "process_count": process_count,
    }
    
while True:
    metrics = collect_metrics()
    
    data ={
        "ip": get_ip(),
        "timestamp": time.time(),
        "metrics": metrics
    }
    
    print(data)
    time.sleep(5)
    

    with open('live_matrics.csv', 'a', newline="") as f:
        write = csv.writer(f)
        write.writerow([
            metrics['cpu'],
            metrics['ram'],
            metrics['network'],
            metrics['process_count']
        ])
        
    time.sleep(5)
