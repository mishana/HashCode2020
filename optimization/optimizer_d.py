import numpy as np
from optimization.optimizer import Optimizer, InData, OutData, LibraryOut
from utils.optimizer_utils import calc_and_save_unique_factor
import os


class OptimizerD(Optimizer):
    def solve(self, in_data: InData) -> OutData:
        UF_PATH = f'./data/saved/uf_{os.environ["filename"]}'

        uf = calc_and_save_unique_factor(in_data, UF_PATH)

        sign_up_times = np.empty(in_data.L)
        total_scores = np.empty(in_data.L)
        time_to_scan = np.empty(in_data.L)

        for i, l in enumerate(in_data.Libraries):

            sign_up_times[i] = l.T
            time_to_scan[i] = l.N / l.M
            # total_scores[i] = np.sum(in_data.Scores[l.Books])
            total_scores[i] = np.dot(in_data.Scores[l.Books], uf[l.Books])
            # total_scores[i] = np.dot(in_data.Scores[l.Books], uf[l.Books]) / time_to_scan[i]  # TODO: only for E

        lib_rate = total_scores
        # lib_rate = total_scores / (sign_up_times + time_to_scan)
        libs_by_rate = lib_rate.argsort()[::-1]

        # build out data
        A = in_data.L
        Libraries = np.empty(len(libs_by_rate), dtype=object)

        for i, l in enumerate(libs_by_rate):
            Y = l
            K = in_data.Libraries[l].N

            lib_books = in_data.Libraries[l].Books
            books = lib_books[lib_books.argsort()[::-1]]
            Libraries[i] = LibraryOut(Y=Y, K=K, Books=books)

        return OutData(A=A, Libraries=Libraries)


