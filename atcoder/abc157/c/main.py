n, m = map(int, input().split())
s = [0] * 5
c = [0] * 5

for i in range(m):
    s[i], c[i]= map(int, input().split())
    s[i] -= 1   # 0-indexed

# n桁を0からチェック
for incr in range(10 ** (n)):
    str_incr = str(incr)  

    # 桁チェック
    if len(str_incr) != n:
        continue

    is_ans = True
    for i in range(m):
        for dig_i in range(n):
            if (dig_i == s[i] and int(str_incr[dig_i]) != c[i]) :
                is_ans = False

    if is_ans:
        print(incr)
        exit(0)

print(-1)
