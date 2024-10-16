

num_test_case = int(input())

def main(price_list):
    save_list = [0 for _ in range(len(price_list))]
    profit = 0
    max_num = -1
    for j in range(len(price_list) - 1, -1, -1):
        if price_list[j] > max_num:
            max_num = price_list[j]
        save_list[j] = max_num

    for k in range(len(price_list)):
        if price_list[k] < save_list[k]:
            profit += save_list[k] - price_list[k]

    return profit

for i in range(num_test_case):
    num_day = int(input())
    price_list = list(map(int, input().split()))

    profit = main(price_list)

    print(f"#{int(i) + 1} {profit}")