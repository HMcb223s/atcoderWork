#!/usr/local/python
q = int(input())

query = []
s = []

for _ in range(q):
  tmp = list(map(int, input().split()))

  if tmp[0] == 1:
    if len(s) == 0:
      s.append(tmp[1])
    elif tmp[1] <= s[0]:
      s.insert(0, tmp[1])
    else:
      for i, x in enumerate(s):
        if tmp[1] >= x:
          continue
        else:
          break
      s.insert(i+1, tmp[1])

  elif tmp[0] == 2:
    for i in range(min(s.count(tmp[1]), tmp[2])):
      s.remove(tmp[1])
  
  if tmp[0] == 3:
    s_len = len(s)
    if s_len == 1:
      print(0)
    if s_len >= 2:
      print(s[s_len-1] - s[0])

#  print(s)
