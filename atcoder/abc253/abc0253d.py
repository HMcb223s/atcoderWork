#!/usr/local/python
n, a, b = list(map(int, input().split()))

tmp = int(n * (n + 1) / 2)

a1, d1, n1= a, a, int(n // a)
a2, d2, n2= b, b, int(n // b)
a3, d3, n3= a * b, a * b, int(n // (a*b))

s1 = int(n1 * (2 * a1 + (n1 - 1) * d1) / 2)
s2 = int(n2 * (2 * a2 + (n2 - 1) * d2) / 2)
s3 = int(n3 * (2 * a3 + (n3 - 1) * d3) / 2)

print(tmp - s1 - s2 + s3)