n = int(input())
d, x = map(int, input().split())

x += n
for i in range(n):
    a = int(input())
    x += (d - 1) // a

print(x)
