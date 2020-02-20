import numpy as np

from optimization.optimizer import Optimizer, InData, OutData, LibraryOut


class OptimizerB(Optimizer):
    def solve(self, in_data: InData) -> OutData:
        sign_up_times = np.empty(in_data.L)
        total_scores = np.empty(in_data.L)
        time_to_scan = np.empty(in_data.L)

        for i, l in enumerate(in_data.Libraries):

            sign_up_times[i] = l.T
            # total_scores[i] = np.sum(in_data.Scores[l.Books])
            # time_to_scan[i] = l.N / l.M

        lib_rate = sign_up_times
        libs_by_rate = lib_rate.argsort()

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


