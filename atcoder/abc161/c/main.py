n, k = map(int, input().split())
x = n % k
print(min(x, k-x))
