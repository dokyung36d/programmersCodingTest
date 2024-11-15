def solution(n, matrix):
    totalSum = 0
    alpha = int((n - 1) / 2)

    for i in range(alpha):
        for j in range(-i, i + 1):
            totalSum += matrix[i][alpha + j]
            totalSum += matrix[n - 1 - i][alpha + j]

    totalSum += sum(matrix[alpha])

    # for i in range(n - 1, alpha, -1):
    #     for j in range(i - )

    return totalSum

T = int(input())
for i in range(1, T + 1):
    n = int(input())

    matrix = []

    for j in range(n):
        newInfo = input()
        newRow = []

        for k in range(n):
            newRow.append(int(newInfo[k]))

        matrix.append(newRow)

    print(f"#{i} {solution(n, matrix)}")
