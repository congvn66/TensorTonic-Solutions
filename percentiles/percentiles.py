import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x)
    x = np.sort(x)
    res = np.percentile(x, q, method='linear')
    return res
        