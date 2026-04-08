import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        matrix = np.array(matrix)
    except Exception:
        return None

    if (len(matrix.shape) == 2) and (matrix.shape[0] == matrix.shape[1]):
        w, v = np.linalg.eig(matrix)
        return w