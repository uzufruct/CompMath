# n - interpolation power
import numpy as np
from random import random


def lagrange(tx, ty, x, n):
    y = 0
    ax = []
    ay = []

    # lookup for the nearest points of x in list
    for i in range(len(tx)):
        if tx[i] <= x < tx[i + 1]:
            k = i
            while k + n >= len(tx):
                k -= 1
            m = k
            for j in range(n + 1):
                ax.append(tx[m])
                ay.append(ty[m])
                m += 1

    # interpolation
    for i in range(n + 1):
        q = 1
        for j in range(n + 1):
            if i != j:
                q *= (x - ax[j])
                q /= (ax[i] - ax[j])
        y += ay[i]*q
    return y


def aitken(tx, ty, x, n):
    # lookup for the nearest points of x in list
    ax = []
    ay = []
    for iter in range(len(tx)):
        if tx[iter] <= x < tx[iter + 1]:
            l = iter
            while l + n + 1 > len(tx):
                l -= 1
            m = l
            for j in range(n + 1):
                ax.append(tx[m])
                ay.append(ty[m])
                m += 1

    def poly(i, j, x):
        if i == j:
            return ay[i]
        else:
            k = 1 / (ax[i] - ax[j])
            return k * (poly(i, j - 1, x) * (x - ax[j]) - poly(i + 1, j, x) * (x - ax[i]))
    return poly(0, n, x)

def newton(tx, ty, x, n):
    q = (x - tx[0]) / n
    p = ty[0]
    k = 1
    for i in range(1, n):
        k /= i
        p += k*ty[i]*q
        q *= (q - 1)