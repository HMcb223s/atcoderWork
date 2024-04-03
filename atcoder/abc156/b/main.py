n, k = map(int, input().split())

cnt = 0

while(n >= k):
    n = n // k
    cnt += 1

cnt += 1
print(cnt)