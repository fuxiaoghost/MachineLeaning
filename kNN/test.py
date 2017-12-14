import numpy as np
import numpy.random as random
mat = random.random(size=(3,3))
min_mat = mat.min(0)
print mat
print min_mat
print mat.shape[0]
print np.tile(min_mat, (mat.shape[0],1))