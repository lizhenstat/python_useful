# GAT中间计算attention的部分
# Cartesian product
import numpy as np
import torch
h = [[1,1,1],[2,2,2],[3,3,3]]
h = torch.tensor(np.array(h))
a_input = torch.cat([h.repeat(1, N).view(N * N, -1), h.repeat(N, 1)], dim=1).view(N, -1, 2 * self.out_features)

# np.add有神奇的现象
a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
a+b # 结果是3x3的矩阵 逐行逐列分别相加

# (3,3,5) * (5,1) 等价于 (9,5) * (5,1)
import numpy as np
import torch
a = np.array([[1,1,1],[2,2,2],[3,3,3]])
a = torch.tensor(a)
a = a.unsqueeze(2)
a = a.repeat(1,1,5)
print(a)
w = torch.tensor(np.array([1,2,3,4,5])).unsqueeze(1)
print(torch.matmul(a,w))

# 等价于以下
b = a.reshape(3*3,5)
torch.matmul(b,w).reshape(3,3,1)
