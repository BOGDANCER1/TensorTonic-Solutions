import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x)
    return x / (1 + np.exp(-x))