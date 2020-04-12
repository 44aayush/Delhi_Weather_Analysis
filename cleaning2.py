import pandas as pd
import numpy as np

a = open("/home/null/Desktop/Python/IDS_project/trail.csv", "r+")
b = open("/home/null/Desktop/Python/IDS_project/trail1.csv", "r+")


lines = a.readlines()

i = 0
for line in lines:
    i = i + 1
    if(i <= 100991):
        x = line.split(",")[7]
        if(x == "-9999.0"):
            x = "NaN"
        for i in range(1,13):
            if(i == 7):
                print(x, end = ",", file = b)
            else:
                print(line.split(",")[i], end = ",", file = b)

