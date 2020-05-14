import math
import numpy as np


class Calc:

    def sum(a, b):
        return a + b

    def difference(a, b):
        return a - b

    def product(a, b):
        return a * b

    def quotient(a, b):
        return a / b

    def log(a, b=None):
        if b is None:
            return math.log(a)
        return math.log(a, b)

    def size(list):
        return np.array(list).size

    def shape(list):
        return np.array(list).shape
