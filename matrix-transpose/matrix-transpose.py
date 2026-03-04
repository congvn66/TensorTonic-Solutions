import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    res = np.zeros((len(A[0]), len(A)))
    for i in range(len(A)):
        for j in range(len(A[i])):
            res[j][i] = A[i][j]

    return res
            
    
