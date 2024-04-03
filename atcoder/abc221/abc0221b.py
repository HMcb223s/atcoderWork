#!/usr/local/python
s = input()
t = input()
t_tmp = t

ans = "No"
n = len(s)

if s == t:
  ans = "Yes"
else:

  for i in range(0, n-1, 1):
    # いったんリストにする
    str_list = list(t)

    tmp = str_list[i+1]
    str_list[i+1] = str_list[i]
    str_list[i] = tmp

    if s == "".join(str_list):
      ans = "Yes"

print(ans)
