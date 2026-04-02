import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    scaling_factor = 1 / (1 - p)
    if rng:
        probs = rng.random(size=np.asarray(x).shape)
    else:
        probs = np.random.random(size=np.asarray(x).shape)
        
    mask = np.where(probs < p, 0, scaling_factor)

    return np.asarray(x) * mask, mask
    