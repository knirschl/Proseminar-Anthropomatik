import numpy as np

UNDEFINED = 0

def expo(x):
    return 1 - np.exp(-x)

def expo_inv(U):
    try:
        return np.log(1/U)
    except ZeroDivisionError:
        return UNDEFINED

def logistic(x):
    return 1/(1 + np.exp(-x))

def logistic_inv(U):
    try:
        return -np.log((1 - U) / U)
    except ZeroDivisionError:
        return UNDEFINED

def cauchy(x):
    return 0.5 + (1 / np.pi) * np.arctan(x)

def cauchy_inv(U):
    return np.tan(U * np.pi)
