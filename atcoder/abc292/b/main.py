n, q = map(int, input().split())
cnt = [0] * n
for _ in range(q):
    e, x = map(int, input().split())
    if e == 1:
        cnt[x-1] += 1
    elif e == 2:
        cnt[x-1] += 2
    elif e == 3:
        if cnt[x-1] >= 2:
            print("Yes")
        else:
            print("No")
