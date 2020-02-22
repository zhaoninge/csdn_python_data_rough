'''
数组切⽚和list切⽚不同之处是，数组切⽚的结果是源数据的视图⽽不是副本
如果想要产⽣源数据的副本，需要⽤到copy函数
'''

import numpy as np

# 如果需要产⽣数据的副本，需要会⽤到copy功能
# 1. 产⽣⼀个数组
a1 = np.zeros(shape=(3, 5))
print("a1 = ", a1)
# 2. 切⽚产⽣新数组,同时使⽤copy产⽣⼀个数据副本
a2 = a1[1:, 1:4].copy()
# 3, 修改切⽚后数组内容
a2[1, 2] = 99
# 4. 查看结果
print("a1 = \n", a1)
print("a2 = \n", a2)

'''
a1 = 
 [[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
a2 = 
 [[ 0.  0.  0.]
 [ 0.  0. 99.]]
'''