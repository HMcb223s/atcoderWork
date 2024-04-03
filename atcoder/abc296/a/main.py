n = int(input())
s = input()

ans = True
for i in range(n - 1):
    if s[i] == s[i+1]:
        ans = False

if ans:
    print("Yes")
else:
    print("No")
