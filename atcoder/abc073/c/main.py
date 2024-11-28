n = int(input())

dict = {}

for _ in range(n):
    num = int(input())
    if num not in dict:
        dict[num] = 1
    else:
        dict.pop(num)

print(len(dict))