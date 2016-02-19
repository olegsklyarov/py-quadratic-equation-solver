from quadratic_solver import QuadraticSolver
from sys import argv


def main():
    if len(argv) == 4:
        a, b, c = map(float, argv[1:4])
        print QuadraticSolver.solve(a, b, c)
    else:
        print "Usage: %s a b c" % argv[0]


if __name__ == '__main__':
    main()
