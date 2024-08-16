s = input()
# print(s)

l, r = 0, 0
cnt = 0

for ch in s:
    if ch == '>':
        r += 1
        cnt += r
    else:
        if r != 0:
            cnt -= min(l, r)
            l, r = 0, 0
        l += 1
        cnt += l

if l != 0 and r != 0:
    cnt -= min(l, r)

print(cnt)
