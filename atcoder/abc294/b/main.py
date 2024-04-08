h, w = map(int, input().split())
for _ in range(h):
    ai = input().split()
    print(''.join([chr(ord('A') + int(x) - 1) for x in ai]).replace('@', '.'))
