def solution(bits):
    cnt = 0
    cur = 0
    for i in range(len(bits)):
        if int(bits[i]) != cur:
            cnt += 1
            cur = 1 - cur

    return cnt

T = int(input())

for _ in range(1, T + 1):
    bits = input()
    result = solution(bits)

    print(f"#{_} {result}")