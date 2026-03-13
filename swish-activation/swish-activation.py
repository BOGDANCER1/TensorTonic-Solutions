import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Implement Swish activation function.
    """
    if isinstance(x, float) or isinstance(x, int):
        return np.array([x / (1 + np.exp(-x))])
    x = np.array(x)
    return x / (1 + np.exp(- x))