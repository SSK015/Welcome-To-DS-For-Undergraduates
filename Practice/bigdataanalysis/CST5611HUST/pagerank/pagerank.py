import numpy as np

if __name__ == '__main__':
    f = open('sent_receive.csv')
    # f = open('receive.csv')
    edges = [line.strip('\n').split(',') for line in f]

    nodes = []
    for edge in edges:
        if edge[1] not in nodes:
            nodes.append(edge[1])
        if edge[2] not in nodes:
            nodes.append(edge[2])

    # print(nodes)

    N = len(nodes)
    L = len(edges)
    # print(N)
    # print(L)
    # 初始化M矩阵
    M = np.zeros([N, N])
    for edge in edges:
        start = nodes.index(edge[1])
        end = nodes.index(edge[2])
        M[end, start] = 1
    # print(M)
    # 构造M矩阵
    for j in range(N):
        sum_of_col = sum(M[:, j])
        for i in range(N):
            if M[i, j]:
                M[i, j] /= sum_of_col
    # print(M)

    r = np.ones(N) / N
    next_r = np.zeros(N)
    # print(r)
    e = 456789
    k = 0
    b = 0.85

    while e > 0.00000001:
        next_r = np.dot(M, r) * b + (1-b) / N * np.ones(N)
        # next_r = np.dot(r, M)
        sum_of_col = sum(next_r)
        next_r = next_r / sum_of_col
        # print(next_r.shape)
        e = next_r - r
        e = max(map(abs, e))
        r = next_r
        k += 1

    print('iteration %s:' % str(k))
    print(r)
