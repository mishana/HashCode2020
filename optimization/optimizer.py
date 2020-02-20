from abc import ABC, abstractmethod
from typing import NamedTuple


class InData(NamedTuple):
    # TODO
    pass


class OutData(NamedTuple):
    # TODO
    pass


class Optimizer(ABC):
    """
    This is an abstract class that represents an optimizer.
    All optimizers (naive, specific etc.) should inherit and implement it.

    Note: inheriting classes might also have some hyper-parameters set in the c'tor, for example.
    """
    @abstractmethod
    def solve(self, in_data: InData) -> OutData:
        pass
