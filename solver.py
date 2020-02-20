from utils.io_utils import read_in, write_out
from optimization.optimizer import Optimizer
from optimization.ExampleOptimizer import ExampleOptimizer
from utils.optimizer_utils import calc_score

IN_DATA_FOLDER = './data/in/'
OUT_DATA_FOLDER = './data/out/'
IN_SUFFIX = '.in'
OUT_SUFFIX = '.out'


if __name__ == '__main__':
    filename = 'a_example'  # TODO: this is just an example
    opt = ExampleOptimizer()  # TODO: this is just an example

    in_data = read_in(IN_DATA_FOLDER + filename + IN_SUFFIX)
    solution = opt.solve(in_data)
    score = calc_score(solution)
    write_out(solution, OUT_DATA_FOLDER + filename + OUT_SUFFIX)

    pass
