import math
from typing import List
from variance.variance import variance, num_friends
import numpy as np

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

print(standard_deviation(num_friends))

sd_np = np.std(num_friends)
print(sd_np)

def standard_deviation_np(xs: List[float]) -> float:
    return np.std(xs)
    
print(standard_deviation_np(num_friends))
