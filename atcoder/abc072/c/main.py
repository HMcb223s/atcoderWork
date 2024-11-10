n = int(input())
a = list(map(int, input().split()))
cnt = [0] * (10**5)

for a_i in a:
    cnt[a_i] += 1

print(max(sum(cnt[i:i+3]) for i in range(10**5 - 2)))
