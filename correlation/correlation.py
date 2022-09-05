from other_things.linear_algebra import dot
from other_things.statistics import de_mean
from standard_deviation.standard_deviation import standard_deviation
from typing import List
import numpy as np

x = [3, 6, 9]
y = [9, 6, 3]

def covariance(xs: List[float], ys: List[float]):
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)

print(covariance(x, y))

def correlation(xs: List[float], ys: List[float]):
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero

print(correlation(x, y))

cor = np.corrcoef(x, y)
print(cor)

def numpy_cor(xs: List[float], ys: List[float]):
    return np.corrcoef(xs, ys)

print(numpy_cor(x, y))

cov = np.cov(x, y)
print(cov)
