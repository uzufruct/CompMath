from math import fabs



def doublecount(fun, a, b, h, eps):
    sum2 = 0
    delta = 4 * eps
    h1 = 2 * h
    while delta >= 3 * eps:
        sum1 = 0
        sum2 = 0
        h1 /= 2
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
        print("Delta:", delta)
    pepe = delta / 3
    print("Eps:", "%3.6f" % pepe)
    print("Previous sum:", sum1)
    return sum2


def simpson(fun, a, b, h, eps):
    sum2 = 0
    delta = 16 * eps
    h1 = 2 * h
    while delta >= 15 * eps:
        h1 /= 2
        h2 = h1 / 2
        n1 = int((b - a) / h1)
        n2 = int((b - a) / h2)
        sum1 = fun(a) + fun(b)
        sum2 = fun(a) + fun(b)
        s11 = 0
        x1 = a + h1
        for i in range(1, n1 - 1, 2):
            s11 += fun(x1)
            x1 += 2 * h1
        s12 = 0
        x1 = a + 2 * h1
        for i in range(2, n1 - 2, 2):
            s12 += fun(x1)
            x1 += 2 * h1
        sum1 += 4 * s11 + 2 * s12
        sum1 *= h1 / 3

        s21 = 0
        x2 = a + h2
        for i in range(1, n2 - 1, 2):
            s21 += fun(x2)
            x2 += 2 * h2
        s22 = 0
        x2 = a + 2 * h2
        for i in range(2, n2 - 2, 2):
            s22 += fun(x2)
            x2 += 2 * h2
        sum2 += 4 * s21 + 2 * s22
        sum2 *= h2 / 3

        delta = fabs(sum2 - sum1)
        print("Delta:", delta)
    pepe = delta / 15
    print("Eps:", "%3.6f" % pepe)
    print("Previous sum:", sum1)
    return sum2