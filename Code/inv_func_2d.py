import numpy as np
import inv_func_1d as idf

'''
  Stack two arrays together as x, y value
'''
def stack(L, L_):
    return np.stack((L, L_), axis=1)

def expo_expo_inv(U):
    return stack(idf.expo_inv(U[:, 0]),
                idf.expo_inv(U[:, 1]))

def expo_logistic_inv(U):
    return stack(idf.expo_inv(U[:, 0]),
                idf.logistic_inv(U[:, 1]))

def logistic_logistic_inv(U):
    return stack(idf.logistic_inv(U[:, 0]),
                idf.logistic_inv(U[:, 1]))

def logistic_sin_inv(U):
    return stack(idf.logistic_inv(U[:, 0]),
                np.arcsin(U[:, 1]))

def sin_expo_inv(U):
    return stack(np.arcsin(U[:, 0]),
                idf.expo_inv(U[:, 1]))

def snrv_inv(U_1): # standard normal random variate
    return stack(np.sqrt(np.log(1/U_1[:, 0])) * np.cos(2 * U_1[:, 1] * np.pi),
                np.sqrt(np.log(1/U_1[:, 0])) * np.sin(2 * U_1[:, 1] * np.pi))

    