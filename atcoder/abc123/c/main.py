n = int(input())
a = [0] * 5

min_a = 10 ** 15
for i in range(5):
    a[i] = int(input())
    min_a = min(min_a, a[i])

# math.ceil(A / B) -> (A + B - 1) // B
min_gropu = (n + min_a - 1) // min_a
ans = 4 + min_gropu
print(ans)
