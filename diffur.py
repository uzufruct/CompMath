from __future__ import print_function
import math
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def fun(x, y, y1der, y2der):
    # Функция из задания
    return (y2der ** 3) + 8 * math.cos(x) * (y2der ** 2) - 7 * math.exp(x) * y1der + 5 * y * (x + 8) - 4 * x


def g(x, y, y1der):
    # Возвращает y''
    a = 1.0
    b = 0.0

    fa = fun(x, y, y1der, a)
    fb = fun(x, y, y1der, b)

    while fa * fb > 0:
        a -= 1
        b += 1
        fa = fun(x, y, y1der, a)
        fb = fun(x, y, y1der, b)

    c = 0
    d = (fb * a - fa * b) / (fb - fa)

    while math.fabs(d - c) > eps:
        c = d
        fc = fun(x, y, y1der, c)
        if fa * fc <  0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        d = (fb * a - fa * b) / (fb - fa)
    return d


def RungeKutta2t(a, b, h, y, y1der):
    # параметры:
    # a, b - границы интервала по x
    # h - шаг по x
    # y - значение функции в точке a(условие задачи Коши)
    # y1der - первая производная функции в точке a(условие задачи Коши)
    # возвращает:
    # значение функции в точке b
    global outy1der
    x = a
    while x < b:
        y_ = y + h * y1der
        y1der_ = y1der + h * g(x, y, y1der)
        y += (h / 2) * (y1der + y1der_)
        y1der += (h / 2) * (g(x, y, y1der) + g(x + h, y_, y1der_))
        x += h

    h = b - x
    y_ = y + h * y1der
    y1der_ = y1der + h * g(b, y, y1der)
    y += (h / 2) * (y1der + y1der_)
    outy1der = y1der + (h / 2) * (g(b, y, y1der) + g(b + h, y_, y1der_))

    return y


def shooting(x0, x1, y0, y1, h):
    alpha = 1.0
    beta = 0

    fa = RungeKutta2t(x0, x1, h, y0, alpha) - y1
    fb = RungeKutta2t(x0, x1, h, y0, beta) - y1

    while fa * fb > 0:
        alpha -= h
        beta += h
        fa = RungeKutta2t(x0, x1, h, y0, alpha) - y1
        fb = RungeKutta2t(x0, x1, h, y0, beta) - y1

    c = 0
    d = (fb * alpha - fa * beta) / (fb - fa)
    print("Shooting:")
    while math.fabs(d - c) > eps:
        c = d
        fc = RungeKutta2t(x0, x1, h, y0, c) - y1
        print("alpha = %2.6f" % alpha, "\tfa = %2.6f" % fa, "\nbeta = %2.6f" % beta,
              "\tfb = %2.6f" % fb, "\nc = %2.6f" % c, "\tfc = %2.6f" % fc)
        if fa * fc < 0:
            beta = c
            fb = fc
        else:
            alpha = c
            fa = fc
        d = (fb * alpha - fa * beta) / (fb - fa)
    return d


def plot_spline(x0, x1, f0, f1, ppp0, ppp1):
        x = np.linspace(x0, x1, 10)

        dx = x1 - x0

        alpha = ppp1 / (6.0 * dx)
        beta = -ppp0 / (6.0 * dx)

        gamma = (-ppp1 * dx * dx / 6.0 + f1) / dx
        eta = (ppp0 * dx * dx / 6.0 - f0) / dx

        p = alpha * (x - x0) ** 3 + beta * (x - x1) ** 3 + gamma * (x - x0) + eta * (x - x1)

        plt.plot(x, p, color="blue")


def splines(tx, ty):
    n = len(tx) - 1
    x = np.array(tx)
    f = np.array(ty)
    dx = x[1] - x[0]

    b = np.zeros(n + 1)
    b[1:n] = (6.0 / dx) * (f[0:n - 1] - 2.0 * f[1:n] + f[2:n + 1])
    b = b[1:n]

    u = np.zeros(n - 1)
    d = np.zeros(n - 1)
    l = np.zeros(n - 1)

    d[:] = 4.0 * dx

    u[:] = dx
    u[0] = 0.0

    l[:] = dx
    l[n - 2] = 0.0

    A = np.matrix([u, d, l])
    xsol = linalg.solve_banded((1, 1), A, b)

    ppp = np.insert(xsol, 0, 0)  # insert before the first element
    ppp = np.insert(ppp, n, 0)  # insert at the end
    plt.scatter(x, f, marker="x")

    for i in range(n):
        # working on interval [i,i+1]
        ppp_i = ppp[i]
        ppp_ip1 = ppp[i + 1]

        f_i = f[i]
        f_ip1 = f[i + 1]

        x_i = x[i]
        x_ip1 = x[i + 1]

        plot_spline(x_i, x_ip1, f_i, f_ip1, ppp_i, ppp_ip1)

    plt.show()


def simpson(x, y, a, b, h, eps):
    n = int((b - a) / h)
    sum1 = (ty[0] ** 2) + (ty[len(ty) - 1] ** 2)
    s11 = 0
    for i in range(1, n - 1, 2):
        s11 += ty[i] ** 2
    s12 = 0
    for i in range(2, n - 2, 2):
        s12 += ty[i] ** 2
    sum1 += 4 * s11 + 2 * s12
    sum1 *= h / 3

    return sum1

eps = 0.001
tx0 = 0.0
ty0 = 4.0
tx1 = 1.0
ty1 = 5.0
th = 0.05

x_nodes = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y_nodes = []

y1der = shooting(tx0, tx1, ty0, ty1, th)
outy1der = 0

for xi in x_nodes:
    y_nodes.append(RungeKutta2t(tx0, xi, th, ty0, y1der))

print("\nTable:")
x = tx0
tx = []
ty = []
while x < tx1 + th:
    y = RungeKutta2t(tx0, x, th, ty0, y1der)
    print("x =", "%2.6f" % x, "\ty(x) =", "%2.6f" % y, "\ty'(x) =", "%2.6f" % outy1der)
    tx.append(x)
    ty.append(y)
    x += th

print("Intergral = %4.6f" % simpson(tx, ty, 0.0, 1.0, th, eps))
y2 = [y ** 2 for y in ty]
plt.plot(tx, ty, marker='o', color='red')
plt.plot(tx, y2, marker='x', color='green')
splines(x_nodes, y_nodes)
plt.show()