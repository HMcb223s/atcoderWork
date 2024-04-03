#!/usr/local/python
l = list(map(int, input().split()))

sorted_l = sorted(l)

if l[1] == sorted_l[1]:
  print("Yes")
else:
  print("No")
