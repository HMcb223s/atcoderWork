#!/usr/local/python

p = list(map(int, input().split()))
alp = "abcdefghijklmnopqrstuvwxyz"

for ch in p :
    print(alp[ch-1], end='')

print("")
