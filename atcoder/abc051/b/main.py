k, s = map(int, input().split())
count = 0
for x in range(k + 1):
    l_y = max(0, s - x - k)   # Y の下限
    h_y = min(k, s - x)       # Y の上限
    if h_y >= l_y:
        count += h_y - l_y + 1

print(count)

# 別解
# count = 0
# for X in range(K + 1):
#   for Y in range(K + 1):
#     z = S - X - Y
#     if 0 <= Z <= K:
#       count += 1
# print(count)
