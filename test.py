import integral
import math

if __name__ == "__main__":
    def f(x):
        return x**3

    print("Trapezium:")
    res = integral.doublecount(f, 0, 7, 0.2, 0.01)
    print("Result:", res)

    print("\nSimpson:")
    res1 = integral.simpson(f, 0, 7, 0.2, 0.01)
    print("Result:", res1)


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