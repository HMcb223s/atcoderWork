n = int(input())

# Check if the price before tax is X, for X = 1, 2, 3, ..., N
ans = -1
for i in range(1, n + 1):
	if int(i * 1.08) == n:
		ans = i

if ans == -1:
	print(":(")
else:
	print(ans)