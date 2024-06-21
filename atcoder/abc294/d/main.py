from collections import deque

n, q = map(int, input().split())
called = deque([])
done = set()
pending = 1

for i in range(0, q):
	query = list(map(int, input().split()))

	if query[0] == 1:
		called.append(pending)
		pending += 1
	elif query[0] == 2:
		done.add(query[1])
	elif query[0] == 3:
		while called[0] in done:
			called.popleft()
		print(called[0])

	# print(query, called)
