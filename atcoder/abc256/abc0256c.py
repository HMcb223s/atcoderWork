#!/usr/local/python
h1, h2, h3, w1, w2, w3 = map(int, input().split())

count = 0
if (h1 + h2 + h3) != (w1 + w2 + w3):
  print(0)

else:
  print(count)