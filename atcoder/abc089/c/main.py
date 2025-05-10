from itertools import combinations
n = int(input())
mymarch = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}

for i in range(n):
    s = input()
    if s[0] in mymarch:
        mymarch[s[0]] += 1

ans = 0
for a, b, c in combinations("MARCH",3):
    # print(f'{a} {b} {c}')
    ans += mymarch[a] * mymarch[b] * mymarch[c]
print(ans)
