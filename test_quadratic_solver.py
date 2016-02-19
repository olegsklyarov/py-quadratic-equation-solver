from unittest import TestCase, main
from quadratic_solver import QuadraticSolver


class TestQuadraticSolver(TestCase):
    def doTest(self, a, b, c, expected):
        self.assertEqual(expected, QuadraticSolver.solve(a, b, c))

    def testBasic(self):
        self.doTest(1, -2, -35, [-5, 7])

    def testNoRoots(self):
        self.doTest(1, -2, 35, [])

    def testLinear(self):
        self.doTest(0, 1, 1, [-1])

    def testConst(self):
        self.doTest(0, 0, 1, [])

    def testManyRoots(self):
        self.doTest(0, 0, 0, "many")

    def testTwoEqualRoots(self):
        self.doTest(1, 2, 1, [-1, -1])

    def testNotNormal(self):
        self.doTest(2, -4, -70, [-5, 7])

if __name__ == '__main__':
    main()
