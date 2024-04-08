n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(a + b)
get_index = {x: i + 1 for i, x in enumerate(c)}

ans_a, ans_b = [], []
for _ in a:
    ans_a.append(get_index[_])
for _ in b:
    ans_b.append(get_index[_])

print(*ans_a)
print(*ans_b)
