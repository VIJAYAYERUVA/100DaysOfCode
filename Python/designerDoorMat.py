def doorMat(N, M):
    top = []
    for i in range(N // 2):
        a = ('.|.' * (2 * i + 1)).center(M, '-')
        top.append(a)
    output = '\n'.join(top + ['WELCOME'.center(M, '-')] + top[::-1])
    print(output)


N, M = map(int, (input().split()))
doorMat(N, M)
