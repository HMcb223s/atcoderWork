a = []
SIZE = 3
for _ in range(SIZE):
    tmp_a = list(map(int, input().split()))
    a.append(tmp_a)

ans = False
marked =  [[False for _ in range(SIZE)] for _ in range(SIZE)]

n = int(input())

# input
for _ in range(n):
    b = int(input())
    for _x in range(SIZE):
        for _y in range(SIZE):
            if a[_x][_y] == b:
                marked[_x][_y] = True

# 横
for x in range(SIZE):
    cnt = 0
    for y in range(SIZE):
        if marked[x][y]:
            cnt += 1
    if cnt == SIZE:
        ans = True

# 縦
for y in range(SIZE):
    cnt = 0
    for x in range(SIZE):
        if marked[x][y]:
            cnt += 1
    if cnt == SIZE:
        ans = True

# 斜め
if SIZE % 2 == 1:
    cnt = 0
    for i in range(SIZE):
        if marked[SIZE - i - 1][i]:
            cnt += 1
    if cnt == SIZE:
        ans = True
    cnt = 0
    for i in range(SIZE):
        if marked[i][i]:
            cnt += 1
    if cnt == SIZE:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
