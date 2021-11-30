from matplotlib.pyplot import errorbar, sca
import numpy as np
import random as rnd

GOLDEN_RATIO_MIN_1 = 0.618033988749894

'''
  Returns a pseudo-random variable in [0.0, 1.0)
'''
def rand01():
    r = 1
    while r == 1:
        r = rnd.uniform(0, 1)
    
    return r

'''
  Returns the next bigger fibonacci number, the next smaller one and 
  the index of the fibonacci number minus 2
'''
def find_next_fibonacci(N):
    f = 1
    fp = 1
    parity = 0
    while (f + fp < N):
        tmp = f
        f += fp
        fp = tmp
        parity += 1
    
    return f, fp, parity

'''
  Generates a golden ratio sequence from a random point 
'''
def golden_set(points, N):
    # set the initial first coordinate
    x = rand01()
    min = x
    idx = 0

    # set the first coordinates
    for i in range(0, N, 1):
        points[i, 1] = x
        
        # keep the minimum
        if (x < min):
            min = x
            idx = i
        
        # increment the coordinate
        x += GOLDEN_RATIO_MIN_1
        if (x >= 1):
            x -= 1
    
    # find the first Fibonacci >= N
    f, fp, parity = find_next_fibonacci(N)
    
    # set the increment and decrement
    inc = fp
    dec = f
    if (parity & 0b1):
        inc = f
        dec = fp

    # permute the first coordinate
    points[0, 0] = points[idx, 1]
    for i in range(1, N, 1):
        if (idx < dec):
            idx += inc
            if (idx >= N):
                idx -= dec
        else:
            idx -= dec
        points[i, 0] = points[idx, 1]
    
    # set the inital second coordinate
    y = rand01()

    # set the second coordinates
    for i in range(0, N, 1):
        points[i, 1] = y

        # increment the coordinate
        y += GOLDEN_RATIO_MIN_1
        if (y >= 1):
            y -= 1

'''
  Generates a golden ratio sequence with 2 dimensions and N points
'''
def generate(N) -> np.ndarray:    
    points = np.full((N, 2), 0, dtype=np.double)
    golden_set(points, N)
    
    return np.array(points, dtype=np.double)
