# 1 ≦ x < 1,000
x = int(input())

coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    count += x // coin
    x %= coin
print(count)
