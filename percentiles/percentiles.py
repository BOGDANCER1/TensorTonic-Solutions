import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Creating sorted array of data points and future answer
    x = np.sort(np.asarray(x))
    percs = np.zeros_like(q, dtype=float)
    # Evaluate the length of data points 
    n = len(x)
    for i in range(len(percs)):
        L = q[i] * (n - 1) / 100
        print(L)
        if np.isclose(L, int(L), atol=1e-06):
            percs[i] = x[round(L)]
        else:
            percs[i] = x[int(L)] + (x[int(L) + 1] - x[int(L)]) * (L - int(L))
    return percs
    