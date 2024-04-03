#!/usr/local/python
s = input()
t = input()

len_s = len(s)
len_t = len(t)

if len_s > len_t:
  print("No")
  exit(0)

flg = True
s_idx = 0

for t_idx in range(len_t):
  if s[s_idx] == t[t_idx]:
    s_idx += 1
    continue

  if s_idx-1 < 0:
    flg = False
    break

  if s[s_idx-2] == s[s_idx-1] and s[s_idx-1] == t[t_idx] and t[t_idx-1] == t[t_idx]:
    while(t_idx < len_t and t[t_idx-1] == t[t_idx]):
      t_idx += 1
  else :
    flg = False
    break


if flg:
  print("Yes")
else:
  print("No")
