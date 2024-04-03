n, a, b = map(int, input().split())
c = list(map(int, input().split()))
sum = a + b
for i in range(n):
    if c[i] == sum:
        print(i+1)
        exit(0)
