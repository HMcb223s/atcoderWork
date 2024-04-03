n, r = map(int, input().split())

# r = x - 100 * (10 - n)
# x = r + 100 * (10 - n)

if n >= 10:
    print(r)
else:
    print(r + 100 * (10 - n))
