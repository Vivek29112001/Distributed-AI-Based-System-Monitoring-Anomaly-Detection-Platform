import numpy as np
import pandas as pd

np.random.seed(42)

#Normal behavior
normal_cpu = np.random.normal(40,5,1000)
normal_ram = np.random.normal(50,7,1000)
normal_net = np.random.normal(200,30,1000)
normal_process = np.random.normal(150,10,1000)

#Anomalies
anomaly_cpu = np.random.normal(90,3,50)
anomaly_ram = np.random.normal(95, 2,50)
anomaly_net = np.random.normal(300,50,50)
anomaly_process = np.random.normal(200,20,50)

cpu = np.concatenate([normal_cpu, anomaly_cpu])
ram = np.concatenate([normal_ram, anomaly_ram])
net = np.concatenate([normal_net, anomaly_net])
process = np.concatenate([normal_process, anomaly_process])

df = pd.DataFrame({
    "cpu": cpu,
    "ram": ram,
    "network": net,
    "process_count": process
})

df.to_csv("server_metrics.csv", index=False)

print("Dataset Created")