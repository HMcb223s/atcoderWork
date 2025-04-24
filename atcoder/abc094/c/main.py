n = int(input())
x = list(map(int, input().split()))

sorted_x = sorted(x)

chu_a = sorted_x[n // 2 - 1]
chu_b = sorted_x[n // 2]
# print(chu_a, chu_b)

for i in range(n):
    if x[i] <= chu_a:
        print(chu_b)
    else:
        print(chu_a)
