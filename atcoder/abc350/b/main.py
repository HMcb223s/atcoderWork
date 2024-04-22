from collections import Counter
n, q = map(int, input().split())
t = list(map(int, input().split()))

ans = n
# list t の数値と出現回数を格納
t_count = Counter(t)
for num, count in t_count.items():
    # print(f"{num}: {count}回")
    if count % 2 == 1:
        ans -= 1

print(ans)
