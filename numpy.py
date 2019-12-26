# non-zero activation
import numpy as np
np.count_nonzero([[[1,2,0,0],[7,0,1,9]],[[1,2,0,0],[7,0,1,8]]])
np.nonzero([[[1,2,0,0],[7,0,1,9]],[[1,2,0,0],[7,0,1,8]]])
# 返回的是每个non-zero element的在每个维度上的index


# string evaluation
eval('5') # 5
myvariable=8
eval('myvariable') # 8
eval('classobject')

import random
foo = ['a', 'b', 'c', 'd', 'e']
# random select one
random.choice(foo)
# random select several(non-overlap)
random.sample(foo, 3)
