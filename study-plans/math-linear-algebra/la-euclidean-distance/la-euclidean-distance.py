import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    return float(np.sqrt(np.sum(np.square(np.array(x) - np.array(y)))))