import numpy as np
import math

a = np.array([180, 172, 178, 185, 190, 195, 192, 200, 210, 190])
ort = np.sum(a) / a.size

std = (np.sum(a)-ort)/a.size -1
print("sdfds",math.sqrt(std))