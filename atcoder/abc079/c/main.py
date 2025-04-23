import itertools


a = list(map(int, input()))
n_op = 3
op_prod = list(itertools.product(['+', '-'], repeat=n_op))
ans = ""

for op in op_prod:
    tmp_sum = a[0]
    for i in range(n_op):
        if op[i] == '+':
            tmp_sum += a[i+1]
        if op[i] == '-':
            tmp_sum -= a[i+1]
    # print(tmp_sum)

    if tmp_sum == 7:
        ans = str(a[0])
        for j in range(n_op):
            ans += str(op[j]) + str(a[j+1])
        ans += "=7"
        break

print(ans)
