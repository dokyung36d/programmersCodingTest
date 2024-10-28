## https://www.codetree.ai/training-field/frequent-problems/problems/codetree-db/description?page=1&pageSize=5

## 출력하는 결과는 오직 rank와 sum
## insert, delete는 순서대로 저장
## 해당되는 범위면 고려

import bisect
from collections import defaultdict

Q = int(input())

main_list = []
insert_list = []
delete_list = []
tree_list = [0] * 100000

def init():
    return []

def insert(menu, price, order):
    global main_list

    bisect.insort_left(main_list, (price, menu, order))
    # bisect.insort_left(insert_list, (price, menu, order))


##삭제한 name이 이후에 추가로 insert 될 수 있음
##모든 name에 대해서 탐색해야 하므로 무조건 O(n) -> 모든 node에 대해 delete가 전달이 되어야 함(-> 진행 시점도 저장해야 함)
## -> Late Propagation 진행
##delete가 올 때마다 탐색하는 각 노드는 delete 여부 확인, 확인하면 대기 list에서 삭제
def delete(name, order):
    global delete_list

    delete_list.append((name, order))

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

def make_tree():
    pass

##sum에서 값을 구할 때 사용했던 값들을 나중에도 사용해야함
def sum(search_list, value, depth, tree_index):
    global tree_list

    total = 0

    if depth == 0: ##미뤄났던 delete를 반영
        index = bisect.insort_left(value)
        apply_deleted((0, index))

    
    if len(search_list) == 1:
        if search_list[0][0] < value:
            return search_list[0][0]
        
        else:
            return 0
        
    if not tree_list:
        make_tree()

    left_list = search_list[:len(search_list) // 2]
    right_list = search_list[len(search_list) // 2:]
    
    mid_value = search_list[len(search_list) // 2]

    if mid_value < value: ##중간값이 원하는 값보다 작을 때
        total += sum(left_list, value, depth + 1, 2 * tree_index + 1)
    
    else:
        left_sum = sum(left_list, value, depth + 1, 2 * tree_index + 1)
        tree_list[2 * tree_index + 1] = left_sum

        total += left_sum
        total += sum(right_list, value, depth + 1, 2 * tree_index + 2)




for i in range(Q):
    command = list(input().split())

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