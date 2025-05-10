n, p = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 1:
        print(2 ** (n - 1))
        exit()

if p == 0:
    print(2 ** n)
else:
    print(0)
