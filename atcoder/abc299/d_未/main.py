n = int(input())

l, r = 1, n
while r - l > 1:
    m = (l + r) // 2
    print(f"? {m}")
    n = int(input())
    if n == 0:
        l = m
    else:
        r = m

print(f"! {l}")
