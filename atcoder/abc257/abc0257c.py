#!/usr/local/python
n = int(input())
s = list(input())
a = list(map(int, input().split()))

if '0' not in s:
  print(n)
  exit(0)
if '1' not in s:
  print(n)
  exit(0)

count = n
chld = 0
adlt = 10000000001
for i in range(n):
  # print("s[i]:", s[i], " a[i] adlt chld", a[i] ,adlt, chld)
  # child
  if s[i] == '0' and  a[i] < adlt:
      chld = max(chld, a[i])
      # print("c, child: ", count, chld)
  # adult
  else:
    if a[i] >= chld:
      adlt = min(adlt, a[i])
      # print("c, adlt: ", count, adlt)

x = adlt - (adlt - chld)

for i in range(n):
  if s[i] == '0' and a[i] > x:
      count -= 1
  elif s[i] == '1' and a[i] >= x:
      count -= 1

print(count)