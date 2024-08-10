import math
import unittest

from src.solver import Solver


class TestSolver(unittest.TestCase):

    def test_no_roots(self):
        (a, b, c) = (1, 0, 1)
        result = Solver.solve(a, b, c)
        self.assertEqual(len(result), 0)

    def test_two_roots(self):
        (a, b, c) = (1, 0, -1)
        result = Solver.solve(a, b, c)
        self.assertEqual(result, (1, -1))

    def test_one_roots(self):
        (a, b, c) = (1, 2, 1)
        result = Solver.solve(a, b, c)
        self.assertEqual(result, (-1, -1))

    def test_zero_div(self):
        (a, b, c) = (0, 1, 1)
        self.assertRaises(ZeroDivisionError, Solver.solve, a, b, c)

    def test_epsilon(self):
        epsilon = 10e-10
        (a, b, c) = (1.0, 2.0 + epsilon, 1.0)
        result = Solver.solve(a, b, c)
        self.assertTrue(math.isclose(result[0], -1))
        self.assertTrue(math.isclose(result[1], -1))

    def test_nan(self):
        self.assertRaises(TypeError, Solver.solve, "1", 1, 1)
        self.assertRaises(TypeError, Solver.solve, 1, "1", 1)
        self.assertRaises(TypeError, Solver.solve, 1, 1, "1")
        self.assertRaises(TypeError, Solver.solve, math.nan, 1, 1)
        self.assertRaises(TypeError, Solver.solve, 1, math.nan, 1)
        self.assertRaises(TypeError, Solver.solve, 1, 1, math.nan)
        self.assertRaises(TypeError, Solver.solve, math.inf, 1, 1)
        self.assertRaises(TypeError, Solver.solve, 1, math.inf, 1)
        self.assertRaises(TypeError, Solver.solve, 1, 1, math.inf)
