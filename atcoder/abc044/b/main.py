w = input()
word = [0] * 26

for ch in w:
    word[ord(ch)- ord('a')] += 1

for a in word:
    if a % 2 == 1:
        print("No")
        exit(0)

print("Yes")