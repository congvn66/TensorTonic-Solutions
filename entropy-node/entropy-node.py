import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    values, counts = np.unique(y, return_counts = True)
    entropy = 0
    for i in counts:
        if i == 0:
            continue
        entropy += -(i / len(y)) * np.log2(i / len(y))
    return entropy