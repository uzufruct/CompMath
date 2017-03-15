from math import sqrt
import numpy as np


def gauss(A, b):
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in range(n - 1):
        for row in range(pivot_row + 1, n):
            multiplier = A[row][pivot_row] / A[pivot_row][pivot_row]
            # Зануляем
            A[row][pivot_row] = 0
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - A[pivot_row][col] * multiplier
            # Модифицируем вектор
            b[row] = b[row] - b[pivot_row] * multiplier
    print(A)
    print(b)
    x = np.zeros(n)
    k = n - 1
    z = np.zeros(1)
    if A[k, k] == z:
        k -= 1
        raise ZeroDivisionError("Matrix is singular.")
    else:
        x[k] = b[k] / A[k, k]
    # Считаем иксы
    while k >= 0:
        if A[k, k] == z:
            raise ZeroDivisionError("Matrix is singular.")
        else:
            x[k] = (b[k] - np.dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
        k -= 1
    return x


def gauss_mdfd(A, b):
    n = len(A)
    # Проверяем размер вектора и матрицы
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for k in range(n - 1):
        # Выбираем максимальный элемент k для поворота
        maxindex = abs(A[k:, k]).argmax() + k
        # Проверяем на вырожденность
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        # Выполняем поворот
        if maxindex != k:
            A[[k, maxindex]] = A[[maxindex, k]]
            b[[k, maxindex]] = b[[maxindex, k]]
            print(A)
            print("--------")
        for row in range(k + 1, n):
            multiplier = A[row][k] / A[k][k]
            A[row][k] = 0
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier * A[k][col]
            # Модифицируем вектор
            b[row] = b[row] - multiplier * b[k]
    print(A)
    x = np.zeros(n)
    k = n - 1
    z = np.zeros(1)
    if A[k, k] == z:
        raise ZeroDivisionError("Matrix is singular.")
    else:
        x[k] = b[k] / A[k, k]
    # Считаем иксы
    while k >= 0:
        if A[k, k] == z:
            raise ZeroDivisionError("Matrix is singular.")
        else:
            x[k] = (b[k] - np.dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
        k -= 1
    return x


def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)
    n_iter = 0
    #Проверка на вырожденность
    for i in range(n):
        s1 = sum(abs(A[i][j]) for j in range(i))
        s2 = sum(abs(A[i][j]) for j in range(i + 1, n))
        if abs(A[i][i]) < (s1 + s2):
            raise ValueError("Matrix is singular.", i)
    converge = False
    while not converge:
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        n_iter += 1
        x = x_new

    print("Iterations:", n_iter)
    return x


def fpi(A, b, eps):
    limit = 100
    diagonal = A.diagonal()

    for i in range(A.shape[0]):
        summ = 0
        for j in range(A[i].size):
            if i != j:
                summ += abs(A[i][j])
        if abs(diagonal[i]) < summ:
            print("Matrix is singular ", diagonal[i], summ)
            exit()

    x = np.zeros_like(b)
    count = 0
    for it_count in range(limit):
        print("Current solution:", x)
        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # Проверяем достигнута ли точность
        if np.allclose(x, x_new, eps):
            break

        x = x_new
        count += 1
    print("Count: ", count)

    return x