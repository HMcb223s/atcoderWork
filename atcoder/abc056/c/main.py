x = int(input())

# t秒後に 0, 1, 2, ..., t*(t+1)/2 がある
# t*(t+1)/2 >= x を満たす最小の t を求める
for i in range(1, 10**6):
    if i * (i + 1) // 2 >= x:
        print(i)
        break

# 別解
# from math import sqrt, ceil
# x = int(input().strip())
# print(ceil(-0.5 + sqrt(1+8*x)/2))