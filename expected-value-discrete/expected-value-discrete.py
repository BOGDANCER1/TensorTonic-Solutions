import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if not np.isclose(sum(np.array(p)), 1, atol=1e-06):
        raise ValueError
    return np.sum(np.asarray(x) * np.asarray(p))
