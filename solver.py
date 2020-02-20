import os

from optimization.optimizer_b import OptimizerB
from optimization.optimizer_c import OptimizerC
from optimization.optimizer_d import OptimizerD
from optimization.optimizer_e import OptimizerE
from utils.io_utils import read_in, write_out
from utils.optimizer_utils import calc_score

IN_DATA_FOLDER = './data/in/'
OUT_DATA_FOLDER = './data/out/'
IN_SUFFIX = '.txt'
OUT_SUFFIX = '.out'


if __name__ == '__main__':
    in_files = ['b_read_on', 'c_incunabula', 'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']

    for f in in_files:
        filename = f  # TODO: this is just an example
        opt = OptimizerE()  # TODO: this is just an example

        os.environ['filename'] = filename

        in_data = read_in(IN_DATA_FOLDER + filename + IN_SUFFIX)
        solution = opt.solve(in_data)
        score = calc_score(solution, in_data)
        print(score)
        write_out(solution, OUT_DATA_FOLDER + filename + OUT_SUFFIX)

    pass
