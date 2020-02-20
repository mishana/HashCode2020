import numpy as np

from optimization.optimizer import InData, OutData


def read_in(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        M, N = lines[0].split()
        slices_per_type = np.array(lines[1].split())

        return InData(M=M, N=N, slices_per_type=slices_per_type)


def write_out(solution: OutData, filename):
    with open(filename, 'w') as f:
        f.write(f'{solution.K}\n')
    with open(filename, 'ab') as f:
        np.savetxt(f, solution.pizza_types.astype(int), fmt='%i')
        pass


if __name__ == '__main__':
    pass
