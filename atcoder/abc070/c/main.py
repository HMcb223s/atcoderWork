import math

n = int(input())
t = [int(input()) for _ in range(n)]
print(math.lcm(*t))
