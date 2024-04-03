#!/usr/bin/env python3
s = input()

cnt = 0
tmp_cnt = 0

for i in s:
    if i in ['A', 'C', 'G', 'T']:
        tmp_cnt += 1
        cnt = max(cnt, tmp_cnt)
    else:
        tmp_cnt = 0

print(cnt)
