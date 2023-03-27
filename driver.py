from scipy.optimize import fsolve
import math
import numpy as np


def sin_squared(x_input):
    return [math.pow((math.sin(x_input[0])), 2)]


def driver():
    root_calculated = (fsolve(sin_squared, np.asarray([3 * math.pi / 4])))
    print('solution found: ', root_calculated[0])
    print('expected solution: ', math.pi)
    print('error: ', np.abs(root_calculated[0] - math.pi))


if __name__ == '__main__':
    driver()
