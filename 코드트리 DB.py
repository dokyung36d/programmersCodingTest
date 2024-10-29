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
tree_list = [(0, defaultdict(int), defaultdict(int), 0)] * len(diverge_list)

for i in range(Q):
    command = list(input().split())
    command_list.append(command)

    if command[0] == "sum":
        bisect.insort_left(diverge_list, command[1])

##(갈라짐의 기준, sum, 자신 아래에서의 name dict)

def init():
    global diverge_list, menu_price_dict, price_menu_dict, tree_list

    diverge_list = []
    menu_price_dict = {}
    price_menu_dict = {}
    tree_list = [(0, defaultdict(int), defaultdict(int), 0)] * len(diverge_list)

def find_path(value):
    global tree_list


    start = 0
    end = len(tree_list) - 1

    return_list = [mid_index]

    while start <= end:
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
    # if price != diverge_list[value_index]: ##각 노드는 K이하 이므로 동일하면 해당 노드에 속함
    #     node = diverge_list[value_index]
    # else:
    #     node = value_index ##경계값과 딱 일치하는 경우
    node = diverge_list[value_index]

    # if price == tree_list[value_index]

    path = find_path(node)

    for i in range(len(path)):
        index = path[i]
        new_dict = tree_list[index][-1]
        if new_dict[menu] == 1 or new_dict[price] == 1:
            print(0)
            break
        new_dict[menu] = 1
        new_dict[price] = 1

        ##추후 delete할 때 사용
        price_menu_dict[price] = menu
        menu_price_dict[menu] = price

        tree_list[index] = (tree_list[index][0], tree_list[index] + price, new_dict, tree_list[index][3] + 1)

    print(1)

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

        tree_list[path[i]] = (tree_list[path[i]][0], tree_list[path[i]][1] - price, node_dict, tree_list[path[i]][3] - 1)



def rank(k):
    global main_list

    start = 0
    end = len(tree_list) - 1

    if tree_list[(start + end) // 2][3] < k:
        return None

    while start <= end:
        index = (start + end) // 2


        left_node_index = (start + index - 1) // 2
        
        if k > tree_list[left_node_index][3]:
            left_node_index = (start + index - 1) // 2
            k -= tree_list[left_node_index][3]

            start = index + 1

            # if k <= 0:
            #     index = left_node_index
            #     break

        elif k <= tree_list[left_node_index][3]:
            end = index - 1


    values = tree_list[index][2].keys()
    price_list = []

    for value in values:
        if type(value) == str:
            continue

        price_list.append(value)

    price_list.sort()

    return price_list[k - 1]

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
    command = command_list[i]

    if command[0] == "init":
        init()

    elif command[0] == "insert":
        insert(command[1], command[2])

    elif command[0] == "delete":
        delete(command[1])

    elif command[0] == "rank":
        rank(command[1])

    elif command[0] == "sum":
        sum(command[1])