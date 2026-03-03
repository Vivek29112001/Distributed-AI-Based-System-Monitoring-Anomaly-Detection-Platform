import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import IsolationForest

np.random.seed(42)

# Normal Data
cpu = np.random.normal(48,10,1000)
ram = np.random.normal(50,8,1000)
network = np.random.normal(20,5 ,1000)

# Create a DataFrame
data = pd.DataFrame({
    "cpu": cpu,
    "ram": ram,
    "network" : network
})

# Inject anomalies
data.iloc[950:960] = [95, 90, 80]

print(data.head())


model = IsolationForest(contamination=0.02)
model.fit(data)

data['anomaly'] = model.predict(data)

print(data["anomaly"].value_counts())


plt.scatter(range(len(data)), data["cpu"], c=data["anomaly"], cmap='coolwarm')
plt.title("CPU Usage with Anomaly Detection")
plt.show()