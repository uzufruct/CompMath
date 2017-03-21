import math
# import sysnonle as sn
import interpolation as inter

if __name__ == "__main__":
    def fun(x):
        return math.pow(math.e, x)


    def table(a, b, h, f, tx, ty):
        d = a
        while d <= b:
            tx.append(d)
            ty.append(f(d))
            d += h

    tx = []
    ty = []
    table(0, 4, 0.5, fun, tx, ty)
    print("\tx\t\tL1(x)\t\tL2(x)\t\tf(x)")
    for i in range(8):
        x = 0.25 + i * 0.5
        print(x, "\t", "%3.5f" % inter.lagrange(tx, ty, x, 1), "\t",
              "%10.5f" % inter.lagrange(tx, ty, x, 2), "\t", "%10.10f" % fun(x))


