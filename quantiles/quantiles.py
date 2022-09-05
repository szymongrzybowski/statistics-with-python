from typing import List
import numpy as np

list_of_values = [1, 2, 3, 4, 5]

def quantile(xs: List[float], p: float) -> float:
    """Returns the quantile value based on pth-percentile."""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

print(quantile(list_of_values, 0.25)) # lower quartile
# result is being rounded up to the nearest integer 

get_quantile = np.quantile(list_of_values, 0.25)
print(get_quantile)
