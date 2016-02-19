from quadratic_solver import QuadraticSolver
from sys import argv


def main():
    if len(argv) == 4:
        print QuadraticSolver.solve(argv[1], argv[2], argv[3])
    else:
        print "Usage: %s a b c" % argv[0]


if __name__ == '__main__':
    main()
