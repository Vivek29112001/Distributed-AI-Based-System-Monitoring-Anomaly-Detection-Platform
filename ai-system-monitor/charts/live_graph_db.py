import requests
import matplotlib.pyplot as plt
import time

url = "http://127.0.0.1:8000/metrics/latest"

while True:
    try:
        r = requests.get(url)

        if r.status_code != 200:
            print("API error:", r.status_code)
            time.sleep(2)
            continue

        data = r.json()

        if not data:
            print("No data in database")
            time.sleep(2)
            continue

        cpu = [d["cpu"] for d in data]
        ram = [d["ram"] for d in data]

        plt.clf()
        plt.plot(cpu, label="CPU")
        plt.plot(ram, label="RAM")

        plt.legend()
        plt.pause(2)

    except Exception as e:
        print("Error:", e)

    time.sleep(3)