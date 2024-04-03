a, b, c = map(int, input().split())
# いずれかが偶数なら0
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:
    print(min(a*b, b*c, c*a))
