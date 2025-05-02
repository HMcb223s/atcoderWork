n = int(input())
w = [input()]

for _ in range(n-1):
    tmp_w = input()
    if tmp_w in w:
        print("No")
        exit()
    if w[-1][-1] != tmp_w[0]:
        print("No")
        exit()
    w.append(tmp_w)
print("Yes")
