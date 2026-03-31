import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X, y = np.array(X), np.array(y)
    w = np.zeros(shape=X.shape[1])
    b = 0
    N = X.shape[0]
    for _ in range(steps):
        p = _sigmoid(X @ w + b)
        w += lr * X.T @ (y - p) / N
        b += lr * np.sum(y - p) / N

    return w, b