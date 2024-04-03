import numpy as np

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

np_a = np.array(a)
np_b = np.array(b)

for i in range(4):
    if np.min(np_b - np_a) >= 0:
        print("Yes")
        exit(0)

    np_a = np.rot90(np_a)
print("No")