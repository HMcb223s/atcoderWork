n = int(input())
a = list(map(int, input().split()))

c_min = 0
cnt_more_3200 = 0
color_cnt = [0] * 8

for ai in a:
    if ai >= 3200:
        cnt_more_3200 += 1
    else:
        idx = ai // 400
        color_cnt[idx] += 1

for _ in range(8):
    if color_cnt[_] > 0:
        c_min += 1

c_max = c_min + cnt_more_3200

if c_min == 0:
    c_min = 1

print(c_min, c_max)
