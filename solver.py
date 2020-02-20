from optimization.NaiveOptimizer import NaiveOptimizer
from utils.io_utils import read_in, write_out
from optimization.optimizer import Optimizer
from utils.optimizer_utils import calc_score

IN_DATA_FOLDER = './data/in/'
OUT_DATA_FOLDER = './data/out/'
IN_SUFFIX = '.txt'
OUT_SUFFIX = '.out'


if __name__ == '__main__':
    filename = 'b_read_on'  # TODO: this is just an example
    opt = NaiveOptimizer()  # TODO: this is just an example

    in_data = read_in(IN_DATA_FOLDER + filename + IN_SUFFIX)
    solution = opt.solve(in_data)
    score = calc_score(solution)
    write_out(solution, OUT_DATA_FOLDER + filename + OUT_SUFFIX)

    pass
