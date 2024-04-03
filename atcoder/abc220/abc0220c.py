#!/usr/local/python
n = int(input())
a = list(map(int, input().split()))
x = int(input())

a_sum = sum(a)

tmp = a_sum * int(x / a_sum)
ans = int(x / a_sum) * len(a)

i = 0
while(x > tmp):
  tmp = tmp + a[i]
  ans = ans + 1
  i = i + 1

print(ans)