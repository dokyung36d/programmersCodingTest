

num_test_case = int(input())

for i in range(num_test_case):
    profit = 0
    num_day = int(input())
    price_list = list(map(int, input().split()))
    save_list = [0 for _ in range(len(price_list))]

    max_num = -1
    for j in range(len(price_list) - 1, -1, -1):
        if price_list[j] > max_num:
            max_num = price_list[j]
        save_list[j] = max_num

    for k in range(len(price_list)):
        if price_list[k] < save_list[k]:
            profit += save_list[k] - price_list[k]

    print(f"#{int(i) + 1} {profit}")
