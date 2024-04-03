#!/usr/local/python
k = int(input())

ans = (21 * 60) + k 
hh = ans // 60
mm = ans % 60

print(f'{hh}:{mm:02}')
