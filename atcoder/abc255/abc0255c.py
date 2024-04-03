#!/usr/local/python
x, a, d, n = map(int, input().split())

min_a = min(a, a + d*n)
max_a = max(a, a + d*n)

# print("x a d n", x, a, d, n)
# print("min",min,"max",max)

if d == 0:
  print(abs(x-a))

elif x >= min_a and x <= max_a:
  # print("(x-a) % d", abs((x-a) % d))
  print( min(abs((x-a) % d), abs((a-x) % d)) ) 

elif x <= min_a:
  print(abs(x - min_a))

elif x >= max_a:
  print(abs(max_a - x))