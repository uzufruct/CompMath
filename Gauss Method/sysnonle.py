def newton(x0, f, fder, eps):
    #fder - производная
    i = 0
    while True:
        # i += 1
        x1 = x0 - (f(x0) / fder(x0))
        if abs(x1 - x0) < eps:
            # print("Iterations:", i)
            return x1
        x0 = x1


def bisection(f, a, b, eps):
    i = 0
    if a > b:
        a, b = b, a
    while abs(b - a) / 2.0 > eps:
        i += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        if f(c) * f(b) < 0:
            a = c
    x = (b - a) / 2
    print("Iterations:", i)
    return x


def chord(f, a, b, eps):
    i = 0
    if a > b:
        a, b = b, a
    c = 0
    while abs(b - a) > eps:
        c = a + (a - b) * f(a) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            if f(c) * f(b) < 0:
                a = c
        i += 1
    print("Iterations:", i)
    return c