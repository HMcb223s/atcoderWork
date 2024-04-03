n = int(input())
s = input()
l = []
r = []

for idx, ch in enumerate(s):
    if ch == 'L':
        r.append(idx)
    else:
        l.append(idx)

print(*(l + [n] + r[::-1]))
