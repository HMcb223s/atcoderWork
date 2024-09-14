from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
# e.g. list(permutations(list(range(1, 4))))
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
mylist = list(permutations(list(range(1, n + 1))))

# print(mylist, p, q)
# print(mylist.index(p), mylist.index(q))
print(abs(mylist.index(p) - mylist.index(q)))
