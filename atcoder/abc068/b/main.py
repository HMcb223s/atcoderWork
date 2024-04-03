n = int(input())

if n <= 1:
    print(1)
    exit(0)

cnt = 1
while(cnt <= n):
    cnt *= 2

print(cnt // 2)
