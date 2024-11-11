s = input()

for i, v in enumerate(s):
    if v.isupper() == True:
        print(i + 1)
        break
