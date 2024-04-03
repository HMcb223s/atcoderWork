#!/usr/local/python
import sys


n = int(input())
l = len(str(n))

if n <= 9:
  print(1)
  sys.exit()

sum = 1
for i in range(1, l, 1):
  print("n:", n)
  print("i:", i)
  mod_n = n % 10

  sum = sum + (l-i-1) * mod_n

  if mod_n != 0:
    sum = sum + 1

  print("mod_n:", mod_n)
  n = n // 10

print("sum:", sum)