n = int(input())
a = list(map(int, input().split()))
b = [True] * n

for i in range(n):
    if(b[i]):
        b[a[i]-1] = False

count = 0
for i in range(n):
    if(b[i]):
        count += 1
print(count)

x = []
for i in range(n):
    if(b[i]):
        x.append(i+1)
print(*x)
