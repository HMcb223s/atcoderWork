n, x = map(int, input().split())
a = set(list(map(int,input().split())))
for value in a:
    if value + x in a:
        print("Yes")
        exit()
print("No")
