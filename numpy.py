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

# python args and kwargs
def myfunc(a,b, *args, **kwargs):
   for ar in args:
      print(ar)
   for ar in kwargs:
       print(ar)
myfunc(1,2,3,4,e='hi',f='we')


# python lambda functions
# x = 'False'
f = lambda x: (str(x).lower() == 'true')
f('True')


# python subprocess with arguments
# -->pickle_dump & pickle_load 
# 如果需要用命令行传object对象时，可以选择传object的保存路径
import pickle
a = {'hello': 'world'}
with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)
print (a == b)


# 子程序要import上一级文件夹的文件
import sys
sys.path.append("E:/CondenseNet/condensenet_new_2")
import models
# 不能用 from ..  import models
# 因为python不认得当前的工作路径
