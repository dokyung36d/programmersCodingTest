def fibonacci(n):
    return_list = [0] * n
    return_list[0] = 1
    return_list[1] = 1

    for i in range(2, n):
        return_list[i] = return_list[i - 1] + return_list[i - 2]

    return return_list


array = fibonacci(2000)
new_array = ["impossible", "BA", "BBA"]

def solution(n):
    new_array = ["impossible", "BA", "BBA"]

    if n < 4:
        return new_array[n - 1]

    if n % 3 == 1:
        return "impossible"

    if n % 3 == 2:
        plusValue = "BBA" * (n // 3)
        return new_array[1] + plusValue

    if n % 3 == 0:
        plusValue = "BBA" * (n // 3)
        return new_array[2] + plusValue


T = int(input())

for _ in range(T):
    n= int(input())
    print(solution(n))
