import math

def solve(a, b, c):
    if any(math.isnan(x) or math.isinf(x) for x in [a, b, c]):
        raise ValueError("коэффициенты должны быть конечными.")

    if abs(a) < 1e-9:
        raise ValueError("коэффициент а не может быть нулём (0)")

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return [x1, x2]
    elif D == 0:
        x = -b / (2 * a)
        return [x, x]
    return []

