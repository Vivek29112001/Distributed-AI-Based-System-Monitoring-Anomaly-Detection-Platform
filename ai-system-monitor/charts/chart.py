import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("data/metrics_log.json", lines=True)

plt.plot(df["cpu"])
plt.title("CPU Usage Over Time")
plt.xlabel("Time")
plt.ylabel("CPU %")

plt.show()