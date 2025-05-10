s = input()
n = len(s)

for i in range(n-4, -1, -2):
    # print(f'{i=}, {s[i+1]=}')
    # print(s[:(i//2+1)] , s[i//2+1:i+2])
    if s[:(i//2+1)] == s[i//2+1:i+2]:
        print(i+2)
        break
