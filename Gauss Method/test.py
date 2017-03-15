# import sysle as s
# import numpy as np
import math
import sysnonle as sn
# import interpolation as inter

if __name__ == "__main__":
    # matrix = np.genfromtxt('matrix.csv', dtype=float, delimiter=',')
    # spl = np.hsplit(matrix, [-1])
    # A_part = spl[0]
    # print(A_part)
    # b_part = spl[1]
    # print(b_part)
    # print('\n------Gauss-----------\n')
    # print(s.gauss(np.copy(A_part), np.copy(b_part)))
    # print('\n------GaussMod--------\n')
    # print(s.gauss_mdfd(np.copy(A_part), np.copy(b_part)))
    # print('\n------Seidel----------\n')
    # print(s.seidel(np.copy(A_part), np.copy(b_part), 0.001))
    # print('\n-------FPI------------\n')
    # print(s.iter(np.copy(A_part), np.copy(b_part), 0.001))
    def fun(x):
        return math.sin(x)

    def fund(x):
        return math.cos(x)

    print(sn.bisection(fun, -0.5, 4, 0.1))
    print(sn.chord(fun, 3, 4, 0.1))
    # print(sn.newton(3, fun, fund, 0.1))
    # tx = [1, 2, 3, 4, 5, 6, 7]
    # ty = [1, 4, 9, 16, 25, 36, 49]
    # print(inter.lagrange(tx, ty, 1.25, 2))

