n = int(input())
a = [int(input()) for _ in range(n)]

button = 1
count = 0

while button != 2:
    button = a[button - 1]
    count += 1
    if count > n:
        print(-1)
        break
else:
    print(count)
