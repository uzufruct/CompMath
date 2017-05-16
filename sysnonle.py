import numpy as np
import scipy.linalg as lg


def newton(x0, f, fder, eps):
    # fder - производная
    i = 0
    while True:
        # i += 1
        x1 = x0 - (f(x0) / fder(x0))
        if abs(x1 - x0) < eps:
            # print("Iterations:", i)
            return x1
        x0 = x1


def solve(A, b):
    [nrows, ncols] = np.shape(A)
    nrows = int(nrows)
    ncols = int(ncols)
    if ncols != nrows:
        print("WARNING: System is not square.")
    P, L, U = lg.lu(A)

    # print(P, L, U)
    # Use forward substitution to solve Ly = Pb
    Pb = np.dot(P, b)
    # print(Pb)
    y = np.array([0.] * ncols)
    for i in np.arange(0, ncols):
        y[i] = (Pb[i] - np.dot(L[i, 0:i], y[0:i])) / L[i, i]

    # Use back-substitution to solve Ux = y
    x = np.array([0.] * ncols)
    for i in range(ncols - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, (i + 1):ncols], x[i + 1:ncols])) / U[i, i]

    return x

"""
Arguments:
- f = function defined on arrays of size m
which returns np.array of size n
- Df = Jacobian matrix of entries for f; n x m
- x0 = initial guess for root; array of size m
- tol = convergence criterion
"""


def newton_n(f, Df, x0, tol):
    xnew = xold = x0
    dx = 1000.
    iters = 0
    max_iters = 1000
    print("initial guess: ", x0)
    while dx > tol:
        if iters > max_iters:
            print("Exceeded {0:3d} iterations without converging".format(max_iters))
            return 0
        deltax = solve(Df(xold), -f(xold))
        xnew = xold + deltax
        dx = np.linalg.norm(deltax)
        xold = xnew
        iters += 1
    print(xnew)
    return xnew


def bisection(f, a, b, eps):
    i = 0
    if a > b:
        a, b = b, a
    while abs(b - a) / 2.0 > eps:
        i += 1
        c = (a + b) / 2
        if f(c) == 0:
            print("Iterations:", i)
            print("Solution:")
            return c
        if f(a) * f(c) < 0:
            b = c
        if f(c) * f(b) < 0:
            a = c
    x = (b - a) / 2
    print("Iterations:", i)
    print("Solution:")
    return x


def chord(f, a, b, eps):
    iter = 1

    def chord_i(f, a, b, eps, iter):
        x = 0
        # if a > b:
        #     a, b = b, a
        while abs(b - a) > eps:
            # a = b - (b - a) * f(b) / (f(b) - f(a))
            # b = a - (a - b) * f(a) / (f(a) - f(b))
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
            if f(c) < 0:
                b = c
            else:
                if f(c) > 0:
                    a = c
                else:
                    if f(c) == 0:
                        print("Iterations C:", iter)
                        print("Solution:")
                        return c
            x = (a + b) / 2
            iter += 1
        print("Iterations:", iter)
        print("Solution:")
        return x

    n = int(abs(b - a) / 0.5)
    ok1 = False
    ok2 = False
    for i in range(n):
        iter += 1
        a += 0.2
        if f(a) > 0:
            ok1 = True
        else:
            if f(a) < 0 and ok1:
                ok1 = False
                return chord_i(f, a - 0.5, a, eps, iter)

        if f(a) < 0:
            ok2 = True
        else:
            if f(a) > 0 and ok2:
                ok2 = False
                return chord_i(f, a - 0.5, a, eps, iter)

