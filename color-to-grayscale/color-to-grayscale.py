import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    H = len(image)
    W = len(image[0])
    res = np.zeros((H, W))
    for i in range(H):
        for j in range(W):
            y = 0.299 * image[i][j][0] + 0.587 * image[i][j][1] + 0.114 * image[i][j][2]
            res[i][j] = y
    return res.tolist()
            