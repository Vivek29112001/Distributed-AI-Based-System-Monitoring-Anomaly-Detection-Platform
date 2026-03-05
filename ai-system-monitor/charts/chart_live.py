import requests
import matplotlib.pyplot as plt
import time

URL = "http://127.0.0.1:8000/metrics-data"

plt.ion()

while True:

    response = requests.get(URL)

    data = response.json()

    cpu = [x["cpu"] for x in data]
    ram = [x["ram"] for x in data]

    plt.clf()

    plt.plot(cpu, label="CPU Usage")
    plt.plot(ram, label="RAM Usage")

    plt.legend()

    plt.pause(2)

    time.sleep(2)