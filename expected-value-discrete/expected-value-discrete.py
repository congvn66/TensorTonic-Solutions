import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    probas = 0
    for pi in p:
        probas = probas + pi

    if probas != 1:
        raise ValueError("no")
    ex = 0
    for i in range(len(x)):
        ex = ex + x[i] * p[i]
    return ex
