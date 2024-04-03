SIZE = 8
for i in range(SIZE):
    s = input()

    x = s.find("*")
    alp = chr(ord('a') + x)

    if x >= 0:
        print(alp, SIZE - i, sep="")
