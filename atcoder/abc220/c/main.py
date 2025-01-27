n = int(input())
a = list(map(int, input().split()))
x = int(input())

a_sum = sum(a)

ans = (x // a_sum) * n

x %= a_sum
for i in a:
    # print(f'{ans=} {x=} {i=}')
    x -= i
    ans += 1
    if x < 0:
        break
print(ans)
