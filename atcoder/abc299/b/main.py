n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

t_cnt = 0
winner_idx = 0
samecolor_max = -1
diffcolor_max = -1

for i in range(n):
    if c[i] == t:
        if samecolor_max < r[i]:
            samecolor_max = r[i]
            winner_idx = i
        t_cnt += 1
    elif t_cnt == 0 and c[i] == c[0]:
        if diffcolor_max < r[i]:
            diffcolor_max = r[i]
            winner_idx = i

print(winner_idx + 1)