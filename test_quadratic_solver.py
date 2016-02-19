from unittest import TestCase, main
from quadratic_solver import QuadraticSolver


class TestQuadraticSolver(TestCase):

    def testBasic(self):
        result = QuadraticSolver.solve(1, -2, -35)
        self.assertEqual([-5, 7], result)

    def testNoRoots(self):
        result = QuadraticSolver.solve(1, -2, 35)
        self.assertEqual([], result)

    def testLinear(self):
        result = QuadraticSolver.solve(0, 1, 1)
        self.assertEqual([-1], result)

    def testConst(self):
        result = QuadraticSolver.solve(0, 0, 1)
        self.assertEqual([], result)

    def testManyRoots(self):
        result = QuadraticSolver.solve(0, 0, 0)
        self.assertEqual("many", result)

    def testTwoEqualRoots(self):
        result = QuadraticSolver.solve(1, 2, 1)
        self.assertEqual([-1, -1], result)

    def testNotNormal(self):
        result = QuadraticSolver.solve(2, -4, -70)
        self.assertEqual([-5, 7], result)


if __name__ == '__main__':
    main()
