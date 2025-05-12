n = int(input())

s_ch_count = [[0] * 26 for _ in range(n)]
for i in range(n):
    s = input()
    for ch in s:
        s_ch_count[i][ord(ch) - ord("a")] += 1

ans = ''
for j in range(26):
    x = s_ch_count[0][j]
    for i in range(n):
        x = min(x, s_ch_count[i][j])
    
    ans += chr(j + ord("a")) * x

print(ans)
