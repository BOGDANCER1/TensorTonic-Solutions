import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    try:
        X = np.asarray(X)
    except Exception:
        return None

    if (len(X.shape) != 2) or (X.shape[0] == 1):
        return None
    
    mu = np.mean(X, axis=0, keepdims=True)
    N = X.shape[0]

    X_cent = X - mu

    return X_cent.T @ X_cent / (N - 1)