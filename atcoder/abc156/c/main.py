n = int(input())
x = list(map(int, input().split()))

x.sort()

# Σ(xi - p)^2 を最大化
# Σ(xi)^2 - 2*Σ(xi)*p + Σ(p)^2 を最大化
# Σ(xi)^2 - 2*Σ(xi)*p + n * p^2 を最大化
# Σ(xi)^2 はpによらない定数 A
# Σ(xi) はpによらない定数 B として
# f(p) = n*p^2 - 2*B*p + A  =  n * (p - B/n)^2 + A - B^2/n
# よって p = B/n のとき最小値をとる
# p を最小化するために、xiの平均値を求める

ans = 99999999
for p in range(101):
    total = 0
    for i in range(n):
        total += (x[i] - p) * (x[i] - p)
        
    ans = min(ans, total)

print(ans)
