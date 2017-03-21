# n - interpolation power
def lagrange(tx, ty, x, n):
    y = 0
    ax = []
    ay = []

    # lookup for the nearest points of x in list
    for i in range(len(tx)):
        if tx[i] < x < tx[i + 1]:
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
