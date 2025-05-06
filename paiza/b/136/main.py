N, H, W = map(int, input().split())
sy, sx = map(int, input().split())
s = input().strip()


def move(y, x, d):
    if d == 'F':
        y -= 1
    elif d == 'B':
        y += 1
    elif d == 'L':
        x -= 1
    elif d == 'R':
        x += 1

    if y < 0 or y >= H or x < 0 or x >= W:
        return -1, -1

    return y, x


c = []
for _ in range(H):
    c.append(list(map(int, input().split())))

# 0-index
sy -= 1
sx -= 1

y_i, x_i = sy, sx
for op in s:
    # print(f'{y_i=}, {x_i=}, {op=}, {c[y_i][x_i]=}')
    y_i, x_i = move(y_i, x_i, op)
    if x_i == -1 or y_i == -1:
        print(-1)
        break

    print(c[y_i][x_i])
