import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    np_v = np.array(v)
    l = [np.sum(np.abs(np_v)), np.sqrt(np.sum(np.square(np_v))), np.max(np.abs(np_v))]
    return np.array(l, dtype=np.float64)