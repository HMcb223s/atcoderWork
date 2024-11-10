h, w = map(int, input().split())

s = ['.' * (w+2)]
for _ in range(h):
    s.append('.' + input() + '.')
s.append('.' * (w+2))
# print(s)

def is_neighbor_dot(i:int, j:int) -> bool:
    if s[i-1][j] == '#':
        return True
    if s[i][j-1] == '#':
        return True
    if s[i+1][j] == '#':
        return True
    if s[i][j+1] == '#':
        return True
    return False

ans_flag = True
for i in range(1, h+1):
    for j in range(1, w+1):
        # print(i, j)
        if s[i][j] == '#' and not is_neighbor_dot(i, j):
            ans_flag = False

if ans_flag:
    print("Yes")
else:
    print("No")
