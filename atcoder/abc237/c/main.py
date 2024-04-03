s = input()
l = len(s) - len(s.lstrip('a'))
r = len(s) - len(s.rstrip('a'))

if l > r :
    print('No')
    exit(0)

rep_s = (r - l) * 'a' + s

if rep_s == rep_s[::-1]:
    print("Yes")
else:
    print("No")
