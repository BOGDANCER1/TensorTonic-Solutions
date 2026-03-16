import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if not y:
        return 0.
    class_count = {}

    for label in y:
        class_count[label] = class_count.get(label, 0) + 1

    entropy = 0
    N = len(y)

    for label, count in class_count.items():
        entropy -= count / N * np.log2(count / N)

    return entropy
    