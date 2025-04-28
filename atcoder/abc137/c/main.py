n = int(input())

ans = 0
s_dict = {}
for i in range(n):
    s = "".join(sorted(input()))

    if s in s_dict:
        s_dict[s] += 1
    else:
        s_dict[s] = 1
    
for k, v in s_dict.items():
    if v > 1:
        ans += v * (v - 1) // 2
print(ans)
