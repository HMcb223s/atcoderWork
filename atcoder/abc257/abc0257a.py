#!/usr/local/python
import math
n, x = map(int, input().split())

ans = int(math.ceil(x / n))

print(chr(ord("A") - 1 + ans))
