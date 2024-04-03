n = int(input())
s = input()

first_flag = False
for i in range(n):
    if first_flag and s[i] == "|":
        first_flag = False
    elif first_flag and s[i] == "*":
        print("in")
        exit(0)
    elif s[i] == "|":
        first_flag = True

print("out")
