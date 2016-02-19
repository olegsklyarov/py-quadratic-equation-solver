from math import sqrt

# y(x) = ax^2 + bx + c
#
# Task solve(a, b, c)
# To find all x (array): y(x) = 0


class QuadraticSolver:

    def __init__(self):
        pass

    @staticmethod
    def solve(a, b, c):

        if a == 0:
            if b == 0:
                if c == 0:
                    return "many"
                return []
            return [-c/b]

        b /= a
        c /= a
        d = b**2/4 - c
        if d < 0:
            return []

        sqrt_d = sqrt(d)
        b /= 2
        return [
            -b - sqrt_d,
            -b + sqrt_d
        ]
