import math
from numbers import Real


class Solver:

    @staticmethod
    def _is_real(v: Real):
        return isinstance(v, Real) and math.isfinite(v)

    @staticmethod
    def solve(a: Real, b: Real, c: Real) -> tuple:

        if not all(map(Solver._is_real, (a, b, c))):
            raise TypeError("Коэффициенты a, b, c должны быть числами")

        if math.isclose(a, 0):
            raise ZeroDivisionError("Коэффициент А не может быть равен 0")

        disc = b ** 2 - 4 * a * c
        if disc < 0:
            return ()
        disc_sqrt = 0 if math.isclose(disc, 0, abs_tol=10e-7) else math.sqrt(disc)
        x1 = (-b + disc_sqrt) / (2 * a)
        x2 = (-b - disc_sqrt) / (2 * a)
        result = (x1, x2)
        return result
