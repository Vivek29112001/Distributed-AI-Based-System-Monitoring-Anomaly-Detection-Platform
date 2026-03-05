import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("live_metrics.csv")

plt.figure()

plt.plot(df["cpu"], label="CPU Usage")
plt.plot(df["ram"], label="RAM Usage")

plt.xlabel("Time Index")
plt.ylabel("Usage %")
plt.title("System Metrics Monitoring")

plt.legend()

plt.show()