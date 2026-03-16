import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    B = np.zeros(shape=A.shape[::-1])

    for i in range(A.shape[0]):
        B[:, i] = A[i, :]

    return B
    
