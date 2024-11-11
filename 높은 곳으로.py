def solution(n, p):
    alpha = ((8 * p + 1) ** (1 / 2) - 1) / 2
    alpha = round(alpha)

    leftValue = (2 * alpha + 1) ** 2
    rightValue = 8 * p + 1

    if leftValue == rightValue and alpha <= n:
        return n * (n + 1) * (1 / 2) - 1

    return n * (n + 1) * (1 / 2)


T = int(input())

for _ in range(T):
    n, p = map(int, input().split())

    print(int(solution(n, p)))

