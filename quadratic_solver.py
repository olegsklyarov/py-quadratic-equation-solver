from math import sqrt


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
            return [-c / b]
        d = b*b - 4*a*c
        if d < 0:
            return []
        sqrt_d = sqrt(d)
        return [(-b - sqrt_d) / (2*a), (-b + sqrt_d) / (2*a)]
