A, B, C, X, Y = map(int, input().split())

# ABピザを2枚買うコストとAピザとBピザをそれぞれ1枚ずつ買うコストを比較
cost = min(A+B, 2*C)

# AピザとBピザの必要な数が多い方を優先して購入
if X > Y:
    total = cost * Y + min(A, 2*C) * (X-Y)
elif X < Y:
    total = cost * X + min(B, 2*C) * (Y-X)
else:
    total = cost * X

print(total)
