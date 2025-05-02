n = int(input())
a = list(map(int, input().split()))

i = 1
cnt = 0
for a_i in a:
    # print(f'{a_i=}, {i=}, {cnt=}')
    if a_i != i:
        cnt += 1
    else:
        i += 1

if cnt == n:
    print(-1)
else:
    print(cnt)
