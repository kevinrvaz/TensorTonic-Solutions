import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a_np = np.array(a)
    b_np = np.array(b)
    mag_a = np.sqrt(np.sum(np.square(a_np)))
    mag_b = np.sqrt(np.sum(np.square(b_np)))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return float(np.dot(a_np, b_np)/(mag_a * mag_b))