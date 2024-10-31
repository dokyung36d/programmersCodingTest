## https://www.codetree.ai/training-field/frequent-problems/problems/codetree-db/description?page=1&pageSize=5

## 출력하는 결과는 오직 rank와 sum
## insert, delete는 순서대로 저장
## 해당되는 범위면 고려

from collections import defaultdict

Q = int(input())

tree_dict = defaultdict(list)

tree_dict[0] = [0, (0, 10 ** 9 + 1), defaultdict(int), defaultdict(str)]


##(갈라짐의 기준, sum, 자신 아래에서의 name dict)

def init():
    global tree_dict

    tree_dict = defaultdict(list)

    ## (전체 sum, 범위, menu_price_dict, price_menu_dict, 자기 아래 갯수)
    tree_dict[0] = [0, (0, 10 ** 9 + 1), defaultdict(int), defaultdict(str), 0]

# def find_path(value):
#     global tree_list


#     start = 0
#     end = len(tree_list) - 1

#     return_list = []

#     while start <= end:
#         mid_index = (start + end) // 2
#         if value == diverge_list[mid_index]:
#             return_list.append(mid_index)
#             break
        
#         if value < diverge_list[mid_index]:
#             end = mid_index - 1
#             return_list.append(mid_index)
        
#         if value > diverge_list[mid_index]:
#             start = mid_index + 1
#             return_list.append(mid_index)

#     return return_list

def apply_node(index, gap, menu, price, insert=True):
    global tree_dict

    if len(tree_dict[index]) == 0:
        local_menu_price_dict = defaultdict(int)
        local_price_menu_dict = defaultdict(str)


        if insert:
            local_menu_price_dict[menu] = price
            local_price_menu_dict[price] = menu

            tree_dict[index] = (price, gap,
                                local_menu_price_dict, local_price_menu_dict, 
                                1)
            
            return
        
        tree_dict[index] = (0, gap,
                            local_menu_price_dict, local_price_menu_dict, 
                            0)
        return
    
    
    local_menu_price_dict, local_price_menu_dict = tree_dict[index][2], tree_dict[index][3]

    local_menu_price_dict[menu] = price
    local_price_menu_dict[price] = menu

    tree_dict[index] = (tree_dict[index][0] + price, tree_dict[index][1],
                            local_menu_price_dict, local_price_menu_dict, 
                            tree_dict[index][-1] + 1)
    
    return

# def check_node_exist(index):
#     global tree_dict

#     if len(tree_dict[index]) == 0:
#         return False
    
#     return True

def insert(menu, price):
    global tree_dict

    index = 0

    if tree_dict[0][2][menu] != 0:
        return 0
    
    if tree_dict[0][3][price] != "":
        return 0

    apply_node(index, (0, 10 ** 9 + 1), menu, price)


    while True:
        # if len(tree_dict[index]) == 0:
        #     pass
        start, end = tree_dict[index][1][0], tree_dict[index][1][1]
        mid_value = (start + end) // 2

        gap = end - start

        left_gap = (start, mid_value)
        right_gap = (mid_value, end)

        if left_gap[0] <= price < left_gap[1]:
            index = 2 * index + 1
            apply_node(index, left_gap, menu, price)

        elif right_gap[0] <= price < right_gap[1]:
            index = 2 * index + 2
            apply_node(index, right_gap, menu, price)


        if gap == 1:
            break

    return 1

##삭제한 name이 이후에 추가로 insert 될 수 있음
##모든 name에 대해서 탐색해야 하므로 무조건 O(n) -> 모든 node에 대해 delete가 전달이 되어야 함(-> 진행 시점도 저장해야 함)
## -> Late Propagation 진행
##delete가 올 때마다 탐색하는 각 노드는 delete 여부 확인, 확인하면 대기 list에서 삭제
##name은 유일함!!!!!!!!!!!!!!!!!!!!!!!!
def delete(menu):
    global tree_dict

    if tree_dict[0][2][menu] == 0:
        tree_dict[0][2].pop(menu)
        return 0
    
    price = tree_dict[0][2][menu]

    index = 0
    
    while True:
        local_menu_price_dict, local_price_menu_dict = tree_dict[index][2], tree_dict[index][3]

        local_menu_price_dict.pop(menu)
        local_price_menu_dict.pop(price)


        tree_dict[index] = (tree_dict[index][0] - price, tree_dict[index][1],
                             local_menu_price_dict, local_price_menu_dict,
                             tree_dict[index][-1] - 1)

        gap = tree_dict[index][1][1] - tree_dict[index][1][0]

        if gap == 1:
            break

        left_node_index = 2 * index + 1
        right_node_index = 2 * index + 2

        left_node = tree_dict[left_node_index]
        right_node = tree_dict[right_node_index]

        if len(left_node) !=0 and left_node[2][menu] != 0:
            index = 2 * index + 1

        elif right_node[2][menu] != 0:
            index = 2 * index + 2



    return price



def rank(k):
    global tree_dict

    if k > tree_dict[0][-1]:
        return None

    index = 0

    while True:
        if tree_dict[index][-1] == 1:
            # price_list = list(tree_dict[index][3].keys())
            # price_list.sort()
            # high_price = price_list[-1]
            # return tree_dict[index][3][high_price]

            price = list(tree_dict[index][3].keys())[0]
            return tree_dict[index][3][price]
        
        # start, end = tree_dict[index][1][0], tree_dict[index][1][1]
        # gap = end - start
        

        left_node_index = 2 * index + 1
        # right_node_index = 2 * index + 2

        # if len(tree_dict[left_node_index]) == 0:
        #     apply_node(left_node_index, (start, (start + end) // 2),
        #                 0, 0, insert=False)

        # if len(tree_dict[right_node_index]) == 0:
        #     apply_node(right_node_index, ((start + end) // 2, end),
        #                 0, 0, insert=False)

        # left_node = tree_dict[left_node_index]


        # right_node = tree_dict[right_node_index]

        # gap = tree_dict[index][1][1] - tree_dict[index][1][0]

        # if gap == 1:
        #     return index + 1
        

        ## 왼쪽 노드가 비어있는 경우 error 발생

        if len(tree_dict[left_node_index]) == 0:
            index = 2 * index + 2
            continue

        if k <= tree_dict[left_node_index][-1]:
            # if k == 1 and left_node[-1] == 1:
            #     key_list = list(tree_dict[index][2].keys())
            #     key_list.sort()
            #     return key_list[0]
            index = 2 * index + 1

        elif k > tree_dict[left_node_index][-1]:
            k -= tree_dict[left_node_index][-1]
            index = 2 * index + 2


## 갈라질 것의 부모의 index를 return
## insert에서 들어오는 value는 전부 다름
# def get_tree_node_index(value):
#     global tree_list

#     path = find_path(value)
    
#     node = tree_list[path[-1]]

#     return node[1]

##sum에서 값을 구할 때 사용했던 값들을 나중에도 사용해야함
def sum(value):
    global tree_dict

    total_sum = 0

    index = 0

    while True:
        start, end = tree_dict[index][1][0], tree_dict[index][1][1]
        gap = end - start

        if gap == 1:
            total_sum += tree_dict[index][0]
            break


        left_node_index = 2 * index + 1
        right_node_index = 2 * index + 2


        # if len(tree_dict[left_node_index]) == 0:
        #     apply_node(left_node_index, (start, (start + end) // 2),
        #                 0, 0, insert=False)

        # if len(tree_dict[right_node_index]) == 0:
        #     apply_node(right_node_index, ((start + end) // 2, end),
        #                 0, 0, insert=False)

        left_node = tree_dict[left_node_index]
        right_node = tree_dict[right_node_index]

        mid_value = (start + end) // 2

        if value >= mid_value:
            index = 2 * index + 2
            if len(left_node) !=0:
                total_sum += left_node[0]
            else:
                pass


            if len(right_node) == 0:
                return total_sum

        elif value < mid_value:
            index = 2 * index + 1

            if len(left_node) == 0:
                return total_sum

    return total_sum


for i in range(Q):
    command = list(input().split())
    if command[0] == "init":
        init()

    elif command[0] == "insert":
        result = insert(command[1], int(command[2]))
        print(result)

    elif command[0] == "delete":
        result = delete(command[1])
        print(result)

    elif command[0] == "rank":
        result = rank(int(command[1]))
        print(result)

    elif command[0] == "sum":
        result = sum(int(command[1]))
        print(result)