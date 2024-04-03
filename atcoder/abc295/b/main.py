import copy


def bomb(x, y):
    result[x][y] = '.'


r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
result = copy.deepcopy(b)

for r_idx in range(r):
    for c_idx in range(c):
        if b[r_idx][c_idx].isnumeric():
            # print(b[r_idx][c_idx])
            power = int(b[r_idx][c_idx])
        else:
            power = -1
        
        for r_pow_idx in range(r):
            for c_pow_idx in range(c):
                if abs(r_idx - r_pow_idx) + abs(c_idx - c_pow_idx) <= power:
                    bomb(r_pow_idx, c_pow_idx)

for r_idx in range(r):
    for c_idx in range(c):
        print(result[r_idx][c_idx], end='')
    print()
