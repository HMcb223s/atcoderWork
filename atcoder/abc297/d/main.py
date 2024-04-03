a, b = map(int, input().split())

ans = 0
if a < b:
    a, b = b, a

while b > 0:
    ans += a // b
    a %= b
    a, b = b, a

ans -= 1

print(ans)
