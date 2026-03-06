from kafka import KafkaConsumer
import json
import os
from ml_model import detect_anomaly

consumer = KafkaConsumer(
    "system_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Kafka Consumer Started...")

data_file = "../data/metrics_log.json"

while True:

    for message in consumer:

        data = message.value

        cpu = data["cpu"]
        ram = data["ram"]

        anomaly = detect_anomaly(cpu, ram)

        data["anomaly"] = anomaly

        print("Received:", data)

        if anomaly:
            print("⚠️ ALERT: Anomaly detected!")

        # save to file
        if not os.path.exists(data_file):
            with open(data_file, "w") as f:
                json.dump([], f)

        with open(data_file, "r+") as f:
            file_data = json.load(f)
            file_data.append(data)
            f.seek(0)
            json.dump(file_data, f, indent=4)