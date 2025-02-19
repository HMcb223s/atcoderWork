s = input()
n = len(s)
x = [0] * n

cnt = 0
for i in range(n):
    if s[i] == 'R':
        cnt += 1
    else:
        x[i] += cnt // 2
        x[i-1] += cnt // 2 + cnt % 2
        cnt = 0

cnt = 0
for i in range(n)[::-1]:
    if s[i] == 'L':
        cnt += 1
    else:
        x[i] += cnt // 2
        x[i+1] += cnt // 2 + cnt % 2
        cnt = 0

print(*x)

# 別解
# s = input()
# n = len(s)
# dp = [[0] * (n + 1) for _ in range(33)]
# for i in range(n):
#     if s[i] == 'R':
#         dp[0][i] = i + 1
#     else:
#         dp[0][i] = i - 1
# for p in range(32):
#     for i in range(n):
#         dp[p + 1][i] = dp[p][dp[p][i]]
# ans = [0] * n
# for i in range(n):
#     ans[dp[32][i]] += 1
# print(*ans)
