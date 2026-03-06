from sklearn.ensemble import IsolationForest
import numpy as np

# simple training dataset
training_data = np.array([
    [20, 40],
    [25, 45],
    [30, 50],
    [35, 55],
    [40, 60],
])

model = IsolationForest(contamination=0.05)

model.fit(training_data)


def detect_anomaly(cpu, ram):

    data = np.array([[cpu, ram]])

    prediction = model.predict(data)

    if prediction[0] == -1:
        return True
    else:
        return False