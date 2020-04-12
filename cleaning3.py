import pandas as pd
import numpy as np

c = open("/home/null/Desktop/Python/IDS_project/trail2.csv", "r+")

df = pd.read_csv("/home/null/Desktop/Python/IDS_project/trail1.csv")

df = df.interpolate()

print(df.to_csv(), file = c)