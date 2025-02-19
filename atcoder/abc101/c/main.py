n, k = map(int, input().split())
a = list(map(int, input().split()))

# ceilは切り上げであり、ceil(x/y)は(x + y - 1) / yで計算ができる
step = (n-1 + k-2) // (k-1)
print(step)
