n = int(input())
s = input()

if s.find("x") >= 0:
    ans = "No"
elif s.find("o") >= 0:
    ans = "Yes"
else:
    ans = "No"

print(ans)