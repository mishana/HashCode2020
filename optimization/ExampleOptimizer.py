from optimization.optimizer import Optimizer, , InData, OutData


class ExampleOptimizer(Optimizer):
    def solve(self, in_data: InData) -> OutData:
        return OutData(K=3, pizza_types=[0, 2, 3])