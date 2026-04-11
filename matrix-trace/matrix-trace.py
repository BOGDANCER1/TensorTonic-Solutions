import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    trace = 0
    A = np.asarray(A)
    for i in range(A.shape[0]):
        trace += A[i, i]

    return trace
