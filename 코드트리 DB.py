import bisect

Q = int(input())

main_list = []
insert_list = []
delete_list = []
tree_list = []

def init():
    return []

def insert(menu, price):
    global main_list

    bisect.insort_left(main_list, (price, menu))
    bisect.insort_left(insert_list, (price, menu))

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
def sum(search_list, value, start = True):
    global tree_list

    total = 0

    if start == True: ##미뤄났던 delete를 반영
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