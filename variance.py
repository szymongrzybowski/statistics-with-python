from typing import List
from scratch.linear_algebra import sum_of_squares
import numpy as np

num_friends = [100, 49, 41, 40, 25]

def mean(xs: List[float]) -> List[float]:
    return sum(xs) / len(xs)

def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    assert len(xs) >= 2, "wariancja wymaga co najmniej dwóch elementów"

    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)

print(variance(num_friends))

variance_np = np.var(num_friends)
print(variance_np)

def variance_np2(xs: List[float]) -> List[float]:
    return np.var(xs)

print(variance_np2(num_friends))
