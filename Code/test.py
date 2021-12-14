import numpy as np
from numpy.core.function_base import linspace
import golden_ratio_sequence as grs
import inv_func_2d as idf2
import plot
import mvn

N = 500

# set rotation matrix pre inversion
rot_matrix = np.array([[1, 0],
                       [0, 1]])

# generate and prepare points U
U = grs.generate(N)
RND = np.transpose(np.array([[grs.rand01() for i in range(N)], [grs.rand01() for i in range(N)]]))
#U = np.matmul(U, rot_matrix)

#plot.plot(idf2.sin_expo_inv(U))
#plot.plot(idf2.snrv_inv(U))

#print(np.shape(idf2.logistic_sin(U)))

#plot.plot(idf2.logistic_sin_inv(U), centered=1, saveTo="idf2_log-sin_iu500c-GRS.pdf")
#plot.plot(idf2.logistic_sin_inv(RND), centered=1, saveTo="idf2_log-sin_iu500c-RND.pdf")
#plot.plot(idf2.logistic_logistic(U))
#plot.plot(idf2.logistic_logistic(RND))

import inv_func_1d as idf1
#p = np.stack((np.linspace(-4, 4), idf1.logistic(np.linspace(-4, 4))), axis=1)
#plot.plot(p)
p = np.stack((np.linspace(0, 1), idf1.logistic_inv(np.linspace(0, 1))), axis=1)
plot.plot(p)




mu = np.array([0.5, 0])
cov_matrix = np.array([[1, 3/5],
                       [3/5, 2]])
'''
mvn1 = mvn.calcP(U, mu, cov_matrix)
plot.plot(mvn1)

coeff = np.array([0.5, 0.5])

plot.plot(points)

pol_coords = []
for (x, y) in points:
    pol_coords.append(plot.cart2pol(x, y))
pol_coords = np.array(pol_coords)
plot.plot(pol_coords, system='pol')'''

'''
a = points[int(grs.rand01() * N), 0]

plot.plotM(np.array([idf2.expo_expo(points),
                    idf2.expo_weibull(points, a),
                    idf2.expo_gumbel(points),
                    idf2.expo_logistic(points)]),
                    titles=['expo expo', 'expo weibull',
                    'expo gumbel', 'expo logistics'])

plot.plot(idf2.expo_expo(points))
'''

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d as plt3
fig = plt.figure()
ax = plt.axes(projection='3d')
_mvn = mvn.calcP(U, mu, cov_matrix)
_mvn3D = np.stack((_mvn, _mvn), axis=0)
c = U[:, 0] + U[:, 1]
ax.scatter(U[:, 0], U[:, 1], _mvn, c=c)

#plt.show()

