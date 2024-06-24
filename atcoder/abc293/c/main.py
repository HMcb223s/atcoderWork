h, w = map(int, input().split())

a = [list(map(int,input().split())) for _ in range(h)]

cnt = 0
n = h + w - 2

for i in range(1<<n):
    s = set()
    s.add(a[0][0])
    r, c = 0, 0
    for j in range(n):
        if i >> j & 1:
            r += 1
        else:
            c += 1
        
        if r >= h or c >=w:
            break
        
        s.add(a[r][c])
    
    if len(s) == n+1:
        cnt += 1
    
    # print("i", i, "s", s)

print(cnt)

