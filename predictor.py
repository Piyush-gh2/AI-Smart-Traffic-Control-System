import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_traffic(df):
    df["t"] = range(1, len(df)+1)
    
    X = df[["t"]]
    y = df["vehicles"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    next_t = np.array([[len(df)+1]])
    prediction = model.predict(next_t)
    
    return prediction[0]