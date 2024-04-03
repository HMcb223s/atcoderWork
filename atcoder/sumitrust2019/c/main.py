X = int(input())
items = [100, 101, 102, 103, 104, 105]

dp = [0] + [-1]*X
for i in range(1, X+1):
    for item in items:
        if i - item >= 0 and dp[i - item] != -1:
            dp[i] = max(dp[i], dp[i - item] + 1)

if dp[X] != -1:
    print(1)
else:
    print(0)
