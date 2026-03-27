import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    s = beta * np.asarray(s) + (1 - beta) * np.abs(g) ** 2
    w = np.asarray(w) - lr * np.asarray(g) / np.sqrt(s + eps)
    return w, s