import numpy as np
from guidetable import GuideTable
import inv_func_1d as if1
import inv_func_2d as if2
import golden_ratio_sequence as grs
import plot as plt

# GLOBAL VARIABLES #
N = 500
func = if1.logistic
func_inv = if1.logistic_inv
max_val = 100
func_dim = 1
table = GuideTable(N, func_inv)

# INITIALIZE VALUES #
uni_rand = grs.generate(N)
table.setup_partial_sums_uniform(func, max_val)

# CALCULATE INVERSION #
#p_rand = [np.array(table.test(uni_rand[:, i])) for i in range(func_dim)]
p_rand = np.array(table.search(uni_rand))

# PLOT #
plt.plot(p_rand)
#plt.plot(func_inv(uni_rand))