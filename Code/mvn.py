import numpy as np

ONE_HALF = 0.5
PI2 = 2 * np.pi

'''
  Stack two arrays together as x, y value
'''
def stack(L, L_):
    return np.stack((L, L_), axis=0)

def exp(x, mu, cov) -> np.double:
    x_min_mu = x - mu
    x_min_mu_T = np.transpose(x_min_mu)
    cov_inv = np.linalg.inv(cov)
    return np.exp(-ONE_HALF * np.matmul(
        np.matmul(x_min_mu_T, cov_inv), x_min_mu))

def p(x, mu, cov) -> np.double:
    n = np.shape(cov)[0]
    return 1/(np.sqrt((PI2 ** n) * np.linalg.det(cov))) * exp(x, mu, cov)

def mix(x, mu, cov, coeff) -> np.double:
    sum = 0
    for k in range(np.shape(mu)[0]):
        sum += coeff[k] * p(x, mu[k], cov[k])
    return sum

def calcP(x, mu, cov) -> np.ndarray:
    n = np.shape(x)[0]
    vec = []
    for i in range(0, n):
        vec.append(p(x[i, :], mu, cov))
    #vec = np.transpose(stack(vec, vec))
    return np.array(vec)