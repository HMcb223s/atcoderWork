n = int(input())
a = list(map(int, input().split()))

x4_c = 0
x2_c = 0
x1_c = 0
for a_i in a:
    if a_i % 4 == 0:
        x4_c += 1
    elif a_i % 2 == 0:
        x2_c += 1
    else:
        x1_c += 1

if max(x2_c, 1) + 2 * x4_c >= n:
    print("Yes")
else:
    print("No")
