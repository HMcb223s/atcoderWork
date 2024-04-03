n = int(input())
w = list(map(str, input().split()))

WORDS = ["and", "not", "that", "the", "you"]

for x in WORDS:
    if x in w:
        print("Yes")
        exit(0)

print("No")
    