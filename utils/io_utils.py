from optimization.optimizer import OutData, InData, LibraryIn, LibraryOut
import numpy as np


def read_in(filename) -> InData:
    with open(filename, 'r') as f:
        first_line = f.readline()
        B, L, D = np.array(first_line.split()).astype(int)
        scores_lines = f.readline()
        scores = np.array(scores_lines.split()).astype(int)
        Libraries = []

        for i in range(L):
            first_line = f.readline()
            second_line = f.readline()
            N, T, M = np.array(first_line.split()).astype(int)
            books = np.array(second_line.split()).astype(int)
            Libraries.append(LibraryIn(N=N, T=T, M=M, Books=books))

    return InData(B=B, L=L, D=D, Scores=scores, Libraries=Libraries)


def write_out(solution: OutData, filename):
    with open(filename, 'w') as f:
        f.write(f'{solution.A}\n')
    for lib in solution.Libraries:
        with open(filename, 'a') as f:
            f.write(f'{lib.Y} {lib.K}\n')
        with open(filename, 'ab') as f:
            np.savetxt(f, lib.Books.astype(int), fmt='%i')


if __name__ == '__main__':
    indata = read_in()
    pass
