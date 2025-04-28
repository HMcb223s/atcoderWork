n = int(input())
d = list(map(int, input().split()))

d.sort()
midian_left = d[n // 2 - 1]
midian_right = d[n // 2]
# N は偶数のみ -> 中央値は d[n // 2 - 1] と d[n // 2] から候補を算出 
# print(f'{midian_left=} {midian_right=}')

if midian_left == midian_right:
    print(0)
else:
    print(midian_right - midian_left)
