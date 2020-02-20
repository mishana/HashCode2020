from abc import ABC, abstractmethod


class Optimizer(ABC):
    """
    This is an abstract class that represents an optimizer.
    All optimizers (naive, specific etc.) should inherit and implement it.

    Note: inheriting classes might also have some hyper-parameters set in the c'tor, for example.
    """
    @abstractmethod
    def solve(self, in_data):
        pass
