import numpy as np

from optimization.optimizer import Optimizer, InData, OutData


class ExampleOptimizer(Optimizer):
    def solve(self, in_data: InData) -> OutData:
        return OutData(K=3, pizza_types=np.array([0, 2, 3], dtype=np.int32).reshape(1, -1))
