import copy
import bisect
from collections import defaultdict

Q = int(input())

top_parent_list = []
# top_parent_most_child_dict = {}
top_parent_layer_dict = {}
node_dict = {}


def node_append(m_id, p_id, color, max_depth):
    global top_parent_list


    if p_id == -1:
        top_parent_list.append([m_id, color, max_depth])
        node_dict[m_id] = [m_id, p_id, color, 0, max_depth, []]
        top_parent_layer_dict[m_id] = defaultdict(list) ##dict 내부에 dict를 생성
        # top_parent_most_child_dict[m_id] = [m_id] ##초기에는 원시 노드도 자식 노드임
        # node_dict[m_id] = [m_id, p_id, color, max_depth, []]
        # return
    else:
        if not check_max_depth(p_id):
            return
        node_dict[p_id][-1].append(m_id)
        current_depth = node_dict[p_id][3] + 1
        node_dict[m_id] = [m_id, p_id, color, current_depth, max_depth, []]


        most_parent_node_id = get_most_parent_id(p_id)
        top_parent_layer_dict[most_parent_node_id][current_depth].append(m_id)
        # index =  bisect.bisect_left(top_parent_most_child_dict[most_parent_node_id])


        # ##새로 들어오는 node의 부모가 기존의 막내이면 해당 list에서 삭제
        # if top_parent_most_child_dict[most_parent_node_id][index] != p_id:
        #     top_parent_most_child_dict[most_parent_node_id].pop(index)
        
        # bisect.insort_left(top_parent_most_child_dict[most_parent_node_id], m_id)



def get_most_parent_id(m_id):
    while m_id != -1:
        most_parent_id = node_dict[m_id][0]
        m_id = node_dict[m_id][1]

    ##m_id는 최고 부모의 m_id
    return most_parent_id

def check_max_depth(p_id):
    depth = 1 ##1의 경우 자지 자신만 허용

    while True:
        depth += 1
        node = node_dict[p_id]

        if depth > node[-2]:
            return False

        if node[1] == -1: ##제일 위의 노드까지 탐색 완료
            return True 
        
        p_id = node_dict[p_id][1] ##부모의 부모


##색깔 변경 여부를 저장하면 좋을 듯 -> 그 아래 하부가 변경되면 대응 불가
def change_color(m_id, color):
    # color = node_dict[m_id][2]

    node_dict[m_id][2] = color

    # bfs_list = copy.deepcopy(node_dict[m_id][-1])
    bfs_list = copy_list(node_dict[m_id][-1])

    while bfs_list:
        node = bfs_list.pop(0)

        node_dict[node][2] = color

        node_child_list = node_dict[node][-1]
        bfs_list.extend(node_child_list)

def search_color(m_id):
    return node_dict[m_id][2]


##위의 색깔 변경 때문에 bfs로 가는 게 좋을 듯
##부모의 색깔만 빼서 가능? -> 불가능할 듯
def get_color_range(m_id):
    color_list = [node_dict[m_id][2]]

    # bfs_list = copy.deepcopy(node_dict[m_id][-1])
    bfs_list = copy_list(node_dict[m_id][-1])

    while bfs_list:
        node = bfs_list.pop(0)

        if node_dict[node][2] not in color_list:
            color_list.append(node_dict[node][2])

        node_child_list = node_dict[node][-1]
        bfs_list.extend(node_child_list)

        if len(color_list) == 5:
            break

    return len(color_list)



#Search Score의 경우 각 Tree의 맨 아래 자식부터 진행하는 것이 시간 상 유리

def search_score_child_first():
    global top_parent_list

    total_score = 0

    for i in range(len(top_parent_list)):
        parent_id = top_parent_list[i][0]

        most_child_list = copy_list(top_parent_most_child_dict[i])



def search_score():
    global top_parent_list

    total_score = 0

    for i in range(len(top_parent_list)):
        parent_id = top_parent_list[i][0]

        total_score += get_color_range(parent_id) ** 2

        # bfs_list = copy.deepcopy(node_dict[parent_id][-1])
        bfs_list = copy_list(node_dict[parent_id][-1])

        while bfs_list:
            node = bfs_list.pop(0)

            total_score += get_color_range(node) ** 2

            bfs_list.extend(node_dict[node][-1])

    return total_score

def copy_list(list1):
    return_list = []

    for thing in list1:
        return_list.append(thing)

    return return_list



print_list = []


for _ in range(Q):
    command = list(map(int, input().split()))

    if command[0] == 100:
        node_append(command[1], command[2], command[3], command[4])

    if command[0] == 200:
        change_color(command[1], command[2])

    if command[0] == 300:
        result = search_color(command[1])
        print_list.append(result)

    if command[0] == 400:
        score = search_score()
        print_list.append(score)

for thing in print_list:
    print(thing)