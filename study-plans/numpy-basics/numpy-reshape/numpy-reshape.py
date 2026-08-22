import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    if operation == "flatten":
        return np.asarray(data, dtype=np.float64).flatten()
    if operation == "transpose":
        return np.transpose(np.asarray(data, dtype=np.float64))
    if operation == "add_batch":
        return np.expand_dims(data, axis=0).astype(np.float64)
