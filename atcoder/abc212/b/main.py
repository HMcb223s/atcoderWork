x = input()

if len(set(x)) == 1:
    print("Weak")
    exit(0)

cnt = 0
for i in range(len(x) - 1):
    a = int(x[i])
    b = int(x[i+1])

    if (b - a) % 10 == 1:
        cnt += 1

if cnt == len(x) - 1:
    print("Weak")
else:
    print("Strong")
