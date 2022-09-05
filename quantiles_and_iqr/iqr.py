from typing import List
from quantiles import quantile, list_of_values

def interquartile_range(xs: List[float]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)

print(interquartile_range(list_of_values))
