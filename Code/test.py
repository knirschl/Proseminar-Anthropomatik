import numpy as np
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

print(np.shape(idf2.logistic_sin(U)))

plot.plot(idf2.logistic_sin(U))
plot.plot(idf2.logistic_sin(RND))
plot.plot(idf2.logistic_logistic(U))
plot.plot(idf2.logistic_logistic(RND))
'''
mu = np.array([0.5, 0])
cov_matrix = np.array([[1, 3/5],
                       [3/5, 2]])
                       
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