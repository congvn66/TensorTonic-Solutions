def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    cur_x = x0
    for step in range(steps):
        cur_d = 2 * a * cur_x + b
        cur_x = cur_x - lr * cur_d

    return cur_x
        