import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    generator = np.random.default_rng(seed)
    if kind == "uniform":
        return generator.random(shape, dtype=np.float64)
    if kind == "normal":
        return generator.standard_normal(shape, dtype=np.float64)
