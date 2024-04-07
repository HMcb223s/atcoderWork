n = int(input())
q = int(input())

d = dict()
box = dict()

for _ in range(q):
    query = list(map(int, input().split()))

    # print(query)

    i = query[1]
    if query[0] == 1:
        j = query[2]
        if j in d.keys():
            d[j].append(i)
        else:
            d[j] = [i]

        if i in box.keys():
            box[i].add(j)
        else:
            box[i] = set([j])
    elif query[0] == 2:
        ans = d[i]
        ans.sort()
        print(*ans)
    else:
        ans = list(box[i])
        ans.sort()
        print(*ans)
