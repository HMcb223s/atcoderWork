n = int(input())
s = input()

# 模範解答
# print(max(map(len, S.split('-'))) if 'o' in S and '-' in S else -1)

ans = tmp = 0
o_flag = False
kushi_flag = False

for i in range(n):
    if s[i] == "-":
        kushi_flag = True
        tmp = 0
    elif s[i] == "o":
        tmp += 1
        o_flag = True
    
    ans = max(ans, tmp)

print(ans) if o_flag and kushi_flag else print(-1)
