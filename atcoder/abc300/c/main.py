h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = [0] * min(h, w)

for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            cnt = 0
            while True:
                if (i + cnt == h) or (j + cnt == w) or (c[i + cnt][j + cnt] == "."):
                    for k in range(cnt):
                        c[i + k][j + cnt - k - 1] = "."
                    ans[(cnt - 1)//2 - 1] += 1
                    break
                c[i + cnt][j +cnt] = "."
                cnt += 1

print(*ans)
