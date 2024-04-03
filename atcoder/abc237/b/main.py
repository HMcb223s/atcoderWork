import numpy as np

h, w = map(int, input().split())
a = [list(map(int, input().split())) for l in range(h)]
matrix = np.array(a).transpose()
for i in range(w):
    for j in range(h):
        print(matrix[i, j], end=' ')

    print()
