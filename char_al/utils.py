
import pandas as pd
import numpy as np

def load_data_to_predict(file, headers, labelEncoder):
    
    df = pd.read_csv(file, header= None)
    df.columns = headers
    
    labels = df["letter"]
    df.drop(columns = "letter",inplace=True)
    Data = df
    
    labels = labelEncoder.transform(labels)
    Data = Data.to_numpy()
    
    return Data, labels