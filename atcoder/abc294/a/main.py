n = int(input())
a = list(map(int, input().split()))
ans = []
for _ in a:
    if _ % 2 == 0:
        ans.append(_)

print(' '.join(map(str, ans)))
