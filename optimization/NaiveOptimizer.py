import numpy as np

from optimization.optimizer import Optimizer, InData, OutData


class NaiveOptimizer(Optimizer):
    def solve(self, in_data: InData) -> OutData:
        sign_up_times = np.empty(in_data.L)
        total_scores = np.empty(in_data.L)
        time_to_scan = np.empty(in_data.L)

        for l in in_data.Libraries:
            sign_up_times[l] = l.T
            total_scores[l] = np.sum(in_data.Scores[l.Books])
            time_to_scan[l] = l.N / l.M

        lib_rate = total_scores / (sign_up_times + time_to_scan)
        libs_by_rate = in_data.Libraries[lib_rate.argsort()[::-1]]

        # build out data
        A = in_data.L


