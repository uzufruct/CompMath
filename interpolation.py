def lagrange(tx, ty, x, n):
    y = 0
    for i in range(n + 1):
        q = 1
        k += 1
        for j in range(n + 1):
            if i != j:
                # print(tx[i], tx[j])
                q *= (x - tx[j])
                q /= (tx[i] - tx[j])
        y += ty[i]*q
    return y