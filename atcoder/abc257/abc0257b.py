#!/usr/local/python
n, k, q = map(int, input().split())

a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i, l_i in enumerate(l):
    if a[l_i-1] == n:
      continue
    else:
      if a[l_i-1]+1 in a:
        continue
      else :
        a[l_i-1] += 1
    
print(' '.join(map(str, a)))