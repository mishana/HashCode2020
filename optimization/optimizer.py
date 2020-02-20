from abc import ABC, abstractmethod
from typing import NamedTuple, Iterable

import numpy as np


class InData(NamedTuple):
    M: int
    N: int
    slices_per_type: np.ndarray


class OutData(NamedTuple):
    K: int
    pizza_types: Iterable[int]


class Optimizer(ABC):
    """
    This is an abstract class that represents an optimizer.
    All optimizers (naive, specific etc.) should inherit and implement it.

    Note: inheriting classes might also have some hyper-parameters set in the c'tor, for example.
    """
    @abstractmethod
    def solve(self, in_data: InData) -> OutData:
        pass
