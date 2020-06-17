# GAT中间计算attention的部分
# Cartesian product
import numpy as np
import torch
h = [[1,1,1],[2,2,2],[3,3,3]]
h = torch.tensor(np.array(h))
a_input = torch.cat([h.repeat(1, N).view(N * N, -1), h.repeat(N, 1)], dim=1).view(N, -1, 2 * self.out_features)
