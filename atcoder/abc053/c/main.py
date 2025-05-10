x = int(input())

base = (x // 11) * 2
rem = x % 11

ans = base
if rem >= 7:
    ans += 2
elif rem >= 1:
    ans += 1

print(ans)
