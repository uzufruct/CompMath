import sysle as s
import numpy as np

if __name__ == "__main__":
    matrix = np.genfromtxt('input.csv', dtype=float, delimiter=' ')
    spl = np.hsplit(matrix, [-1])
    A_part = spl[0]
    print(A_part)
    b_part = spl[1]
    print(b_part)
    print('\n------------------\n')
    print(s.gauss(np.copy(A_part), np.copy(b_part)))
    print('\n------------------\n')
    print(s.gauss_mdfd(A_part, b_part))
    print('\n------------------\n')
    print(s.seidel(A_part, b_part, 0.01))