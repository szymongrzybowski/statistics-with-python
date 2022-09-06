from typing import List
from other_functions.linear_algebra import sum_of_squares
from other_functions.statistics import de_mean
import numpy as np

num_friends = [100, 49, 41, 40, 25]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2, "variance requires at least two elements of the set"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)

print(variance(num_friends))

variance_np = np.var(num_friends)
print(variance_np)

def variance_np2(xs: List[float]) -> List[float]:
    return np.var(xs)

print(variance_np2(num_friends))
