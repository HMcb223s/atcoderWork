n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
alice = 0
bob = 0
for i, x in enumerate(a):
    if i % 2 == 0:
        alice += x
    else:
        bob += x

print(alice - bob)
