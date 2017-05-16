# import numpy as np
# import sysnonle as sn
import math
import interpolation as inter
from matplotlib import pyplot as plt
import matplotlib.collections as mcol

if __name__ == "__main__":

    def fun(x):
        return math.sin(x)

    tx = []
    ty = []
    x = []
    y = []
    ya = []

    a = -math.pi
    b = math.pi
    h = 0.01
    h2 = math.pi / 2
    n = int(abs(b - a) / h)
    n2 = int(abs(b - a) / h2)


    for i in range(n2 + 1):
        x.append(a + i * h2)
        y.append(fun(x[i]))



    for i in range(n):
        tx.append(a + i * h)
        ty.append(fun(tx[i]))

    for i in range(n):
        ya.append(inter.aitken(x, y, tx[i], 2))

    plt.figure()
    plt.title('Interpolation', fontsize=14)
    plt.ylabel('y')
    plt.xlabel('x')
    colors = ['red', 'green', 'blue']
    styles = ['solid', 'solid', 'solid']
    lines = []
    lbl = ['f(x)', 'Lagrange', 'Aitken']

    plt.plot(tx, ty, c=colors[0], ls='solid', label=lbl[0])
    plt.plot(tx, ya, c=colors[2], ls='solid', label=lbl[2])
    # for i, color, style in zip(range(1, 4), colors, styles):
    #     # if i != 1:
    #     #     lbl = "n = {0}".format(int(number[i - 1]))
    #     # else:
    #     #     lbl = "Linear speedup"
    #     plt.plot(data[0], data[i], c=color, ls=style, label=lbl[i - 1], marker='o')

    # make proxy artists
    # make list of one line -- doesn't matter what the coordinates are
    line = [[(0, 0)]]
    # set up the proxy artist
    lc = mcol.LineCollection(4 * line, linestyles=styles, colors=colors)
    # create the legend
    plt.legend(shadow=True, fancybox=True)

    plt.show()


# def f(x):
#     out = np.array([x[1]*x[0]**2 - 4, x[0]/(x[1]**2) - 2])
#     return out
#
#
# def Df(x):
#     out = np.array([[2*x[0]*x[1], x[0]**2], [1/(x[1]**2), -2 * x[0] / (x[1]**3)]])
#     return out
#
# if __name__ == '__main__':
#     try:
#         x = sn.newton_n(f, Df, [0.5, 0.5], 0.1)
#         print("final value:", x)
#         # print("f(", x, ") = ", f(x))
#     except ZeroDivisionError:
#         print("Oops, divided by zero.")
#         print("Try again with different initial guess.")