n = int(input())
x = [*map(int, input().split())]
x.sort()

sum = 0
for i in range(3 * n):
    sum += x[n + i]

print(sum / (3 * n))
