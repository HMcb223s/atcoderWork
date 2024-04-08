a, b, c = map(int, input().split())
# MAX = 100000
cnt = 0
while a % 2 == 0 and b % 2 == 0 and  c % 2 == 0:
    if a == b and b == c:
        cnt = -1
        break

    na = b // 2 + c // 2
    nb = a // 2 + c // 2
    nc = a // 2 + b // 2
    a, b, c = na, nb, nc
    cnt += 1
    # print(a, b, c)

print(cnt)
