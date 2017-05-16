from math import fabs


def doublecount(fun, a, b, h1, eps):
    sum2 = 0
    delta = 4 * eps
    while delta >= 3 * eps:
        sum1 = 0
        sum2 = 0
        h2 = h1 / 2
        n1 = int((b - a) / h1)
        n2 = int((b - a) / h2)
        x1 = a + h1
        x2 = a + h2
        for i in range(1, n1 - 1):
            sum1 += fun(x1)
            x1 += h1
        sum1 += (fun(a) + fun(b)) / 2
        sum1 *= h1
        for i in range(1, n2 - 1):
            sum2 += fun(x2)
            x2 += h2
        sum2 += (fun(a) + fun(b)) / 2
        sum2 *= h2
        delta = fabs(sum2 - sum1)
    return sum2
