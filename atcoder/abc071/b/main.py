s = input()
a2z = 'abcdefghijklmnopqrstuvwxyz'

for ch in a2z:
    if ch not in s:
        print(ch)
        exit()
print('None')
