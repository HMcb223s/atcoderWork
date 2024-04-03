#!/usr/local/python
s = input()

max = s
min = s

n = len(s)

for i in range(n):
  s.insert(n, s[0])
  s.pop(0)
  if min > s:
    min = s
  if max < s:
    max = s

  print(s)

print(min)
print(max)