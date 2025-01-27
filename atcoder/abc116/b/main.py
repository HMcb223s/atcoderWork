s = int(input())
s_set = {s}

f = s
for i in range(2, 1000001):
    if f % 2 == 0:
        f = f // 2
    else:
        f = f * 3 + 1
    
    if f in s_set:
        break

    s_set.add(f)
    # print(f, s_set)
print(i)
