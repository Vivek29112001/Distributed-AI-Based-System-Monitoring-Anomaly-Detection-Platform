from kafka import KafkaProducer
import json
import time
import socket
import psutil

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


def collect_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    network = psutil.net_io_counters().bytes_sent
    process_count = len(psutil.pids())
    timestamp = time.time()

    data = {
        "cpu": cpu,
        "ram": ram,
        "network": network,
        "process_count": process_count,
        "ip": ip_address,
        "timestamp": timestamp
    }

    return data


print("Kafka Producer Started...")

while True:
    metrics = collect_metrics()

    producer.send("system_metrics", metrics)

    print("Sent:", metrics)

    time.sleep(5)