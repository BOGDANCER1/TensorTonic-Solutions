import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    G = np.asarray(G) + np.asarray(g) ** 2
    w = np.asarray(w) - lr / (np.sqrt(G + eps)) * np.asarray(g)

    return w, G