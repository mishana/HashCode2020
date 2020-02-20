from collections import defaultdict

import numpy as np

from optimization.optimizer import OutData, InData
import _pickle as pickle

def calc_score(solution: OutData, in_data: InData) -> float:
    T = 0
    scanned_books = set()

    for l in solution.Libraries:
        T += in_data.Libraries[l.Y].T
        days_of_scan = in_data.D - T

        books_to_scan = set(l.Books[:(days_of_scan * in_data.Libraries[l.Y].M)])
        scanned_books = scanned_books | books_to_scan

    score = 0
    for b in scanned_books:
        score += in_data.Scores[b]

    return score


def calc_and_save_unique_factor(in_data: InData, savepath: str):
    import os
    savepath = f'{savepath}.npy'
    if os.path.exists(savepath):
        # with open(savepath, 'rb') as f:
        #     return pickle.load(f)
        return np.load(savepath)


    counter = defaultdict(float)

    for l in in_data.Libraries:
        for b in l.Books:
            counter[b] += 1

    keys = list(counter.keys())
    values = list(counter.values())

    arr = np.empty(in_data.B)
    arr[keys] = values

    arr = 1 - (arr / in_data.L)

    # with open(savepath, 'wb') as f:
        # pickle.dump(arr, f)
    np.save(savepath, arr)

    return arr

# MORE FUNCTIONS THAT ARE COMMON FOR DIFFERENT OPTIMIZERS ARE GOING TO BE PLACED HERE