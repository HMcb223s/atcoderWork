N = int(input())
b = []
for _ in range(N):
    b.append(list(map(int, input().split())))
    # print(*b[_])


def spiral_order(matrix):
    result = []
    while matrix:
        # 上 左から右
        result += matrix.pop(0)
        # 右 上から下
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        # 下 右から左(逆順)
        if matrix:
            result += matrix.pop()[::-1]
        # 左 下から上(逆順)
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    # print(f'spiral_order: {result=}')
    return result


katori = spiral_order(b)
check_idx = [N * N // 4, N * N // 2, N * N * 3 // 4]
# print(f'{check_idx=}')

sum = 0
for i in range(len(katori)):
    if i in check_idx:
        print(sum)
    sum += katori[i]
    # print(f'{i=}, {katori[i]=}, {sum=}')
print(sum)
