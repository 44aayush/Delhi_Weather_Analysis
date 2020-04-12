import pandas as pd
import numpy as np

a = open("/home/null/Desktop/Python/IDS_project/trail.csv", "r+")

df = pd.read_csv("/home/null/Desktop/Python/IDS_project/test.csv")

df.drop(df.columns[[4, 7, 9, 10, 12, 13, 17, 18]], axis=1, inplace=True)

df = df.interpolate()

print(df.to_csv(), file=a)

