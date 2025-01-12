import pandas as pd
import numpy as np
regions = []
delta = []
with open('regions.txt') as file:
    lines = file.readlines()
    for line in lines:
        regions.append(line.split())
regions = np.array(regions, np.float64)
with open('delta.txt') as file1:
    lines1 = file1.readlines()
    for line1 in lines1:
        delta.append(line1.split(', '))
delta = np.array(delta, np.int16)
res = (regions + delta) * 1.07
print(res)