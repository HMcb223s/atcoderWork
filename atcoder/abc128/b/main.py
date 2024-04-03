n = int(input())

guidebook = list()
for i in range(n):
    s, p = input().split()
    guidebook.append([s, -int(p), i+1])

guidebook.sort()
for i, v in enumerate(guidebook):
    print(v[2])
