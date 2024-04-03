#!/usr/local/python
n, q = map(int, input().split())
s = input()

for _ in range(q):
  t, x = map(int, input().split())

  tmp = ''
  if t == 1:
    # print(s[:(n-x)])
    # print(s[((-1)*(x)):])
    tmp = s[((-1)*(x)):] + s[:(n-x)]
    # print(tmp)
    s = tmp
  elif t == 2:
    print(s[(x-1)])
    