#!/usr/local/python

N = int(input())

raw_s = set()
for _ in range(N):
  x, y = map(int, input().split())
  raw_s.add((x, y))

s = sorted(raw_s)

# print(s)

ans = 0
for i in range(N):
  for j in range(N):
    if s[i][0] < s[j][0] and s[i][1] < s[j][1] :
      if (s[i][0], s[j][1]) in s :
        if tuple([s[j][0], s[i][1]]) in s :
          ans += 1

print(ans)