from abc import ABC, abstractmethod
from typing import NamedTuple, List
import numpy as np

class InData(NamedTuple):
    B: int
    L: int
    D: int
    Scores: np.ndarray
    Libraries: List[LibraryIn]
    
class LibraryIn(NamedTuple):
    N: int
    T: int
    M: int
    Books: np.ndarray


class OutData(NamedTuple):
    A: int
    Libraries: List[LibraryOut]
    
class LibraryOut(NamedTuple):
    Y: int
    K: int
    Books: np.ndarray


class Optimizer(ABC):
    """
    This is an abstract class that represents an optimizer.
    All optimizers (naive, specific etc.) should inherit and implement it.

    Note: inheriting classes might also have some hyper-parameters set in the c'tor, for example.
    """
    @abstractmethod
    def solve(self, in_data: InData) -> OutData:
        pass
