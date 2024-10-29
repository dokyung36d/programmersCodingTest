## https://www.codetree.ai/training-field/frequent-problems/problems/codetree-db/description?page=1&pageSize=5

## 출력하는 결과는 오직 rank와 sum
## insert, delete는 순서대로 저장
## 해당되는 범위면 고려

import bisect
from collections import defaultdict

Q = int(input())

command_list = []
diverge_list = []
menu_price_dict = {}
price_menu_dict = {}

for i in range(Q):
    command = list(input().split())
    command_list.append(command)

    if command[0] == "sum":
        bisect.insort_left(diverge_list, command[1])

tree_list = [(0, defaultdict(int), defaultdict(int))] * len(diverge_list)
##(갈라짐의 기준, sum, 자신 아래에서의 name dict)

def init():
    return []

def find_path(value):
    global tree_list


    start = 0
    end = len(tree_list) - 1

    return_list = [mid_index]

    while True:
        mid_index = (start + end) // 2
        if value == diverge_list[mid_index]:
            return_list.append(mid_index)
            break
        
        if value < diverge_list[mid_index]:
            end = mid_index - 1
            return_list.append(mid_index)
        
        if value > diverge_list[mid_index]:
            start = mid_index + 1
            return_list.append(mid_index)

    return return_list


def insert(menu, price):
    global diverge_list

    value_index = bisect.bisect_left(diverge_list, price)
    if price != diverge_list[value_index]: ##각 노드는 K이하 이므로 동일하면 해당 노드에 속함
        node = diverge_list[value_index]
    else:
        node = value_index ##경계값과 딱 일치하는 경우

    path = find_path(node)

    for i in range(len(path)):
        index = path[i]
        new_dict = tree_list[index][-1]
        if new_dict[menu] == 1 or new_dict[price] == 1:
            break
        new_dict[menu] = 1
        new_dict[price] = 1

        ##추후 delete할 때 사용
        price_menu_dict[price] = menu
        menu_price_dict[menu] = price

        tree_list[index] = (tree_list[index][0], tree_list[index] + price, new_dict)



##삭제한 name이 이후에 추가로 insert 될 수 있음
##모든 name에 대해서 탐색해야 하므로 무조건 O(n) -> 모든 node에 대해 delete가 전달이 되어야 함(-> 진행 시점도 저장해야 함)
## -> Late Propagation 진행
##delete가 올 때마다 탐색하는 각 노드는 delete 여부 확인, 확인하면 대기 list에서 삭제
##name은 유일함!!!!!!!!!!!!!!!!!!!!!!!!
def delete(menu):
    global tree_list, menu_price_dict

    price = menu_price_dict[menu]

    if price == 0:
        return 0
    

    ## 각 price는 unique하므로 바로 index를 구할 수 있음
    index = bisect.bisect_left(tree_list, price)
    node_value = tree_list[index]
    path = find_path(node_value)

    for i in range(len(path)):
        node = tree_list[path[i]]
        node_dict = node[2]

        node_dict[menu] = 0
        node_dict[price] = 0

        tree_list[path[i]]


def apply_deleted(start_index, end_index):
    global main_list, delete
    pass

def rank(k):
    global main_list

    apply_deleted((0, k))

    if len(main_list) >= k:
        print("None")
        return
    
    print(main_list[k-1][1])

## 갈라질 것의 부모의 index를 return
## insert에서 들어오는 value는 전부 다름
def get_tree_node_index(value):
    global tree_list

    path = find_path(value)
    
    node = tree_list[path[-1]]

    return node[1]

##sum에서 값을 구할 때 사용했던 값들을 나중에도 사용해야함
def sum(value):
    global tree_list, diverge_list

    mid_index = len(tree_list) // 2

    while True:
        if value == diverge_list[mid_index]:
            break
        
        if value < diverge_list[mid_index]:
            mid_index = (0 + mid_index) // 2
        
        if value > diverge_list[mid_index]:
            mid_index = (len(tree_list) + mid_index) // 2

    return tree_list[mid_index][0]
 



for i in range(Q):
    if command[0] == "init":
        main_list = init()

    elif command[0] == "insert":
        insert()

    elif command[0] == "delete":
        delete()

    elif command[0] == "rank":
        rank()

    elif command[0] == "sum":
        sum()