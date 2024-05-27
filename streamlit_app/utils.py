import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def load_mock_data():
    dates = [datetime.today() - timedelta(days=i) for i in range(10)]
    data = {
        'Date': dates,
        'Metric A': np.random.randint(0, 100, 10),
        'Metric B': np.random.randint(0, 100, 10),
        'Metric C': np.random.randint(0, 100, 10)
    }
    return pd.DataFrame(data)

def load_data(filepath):
    return pd.read_csv(filepath)

def load_readme():
    with open("README.md", "r") as file:
        return file.read()
