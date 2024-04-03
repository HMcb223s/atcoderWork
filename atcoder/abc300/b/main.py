from collections import deque

# def print2(x):
#     for i in range(len(x)):
#         print("".join(x[i]))
#     print("\n")

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]

flag = False

for i in range(h):
    for j in range(w):
        # print2(a)
        if a == b:
            flag = True 

        for k in range(h):
            a[k].append(a[k][0])
            del a[k][0]

    a.append(a[0])
    del a[0]

print("Yes" if flag else "No")
