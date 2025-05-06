import  math

n, x_first = map(int, input().split())
x = list(map(int, input().split()))
fixed_x = [(_ - x_first) for _ in x]

print(math.gcd(*fixed_x))
