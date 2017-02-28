def newton(x0, f, fder, eps):
    #f1 - производная
    while True:
        x1 = x0 - (f(x0) / fder(x0))
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1
