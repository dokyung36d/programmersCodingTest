Q = int(input())

top_parent_list = []
node_dict = {}


def node_append(m_id, p_id, color, max_depth):
    global top_parent_list

    if m_id == -1:
        top_parent_list.append([m_id, color, max_depth])
        return
    
    node_dict.append([m_id, p_id, color, max_depth, []])
    node_dict[p_id][-1].append(m_id)

def check_max_depth(p_id):
    depth = 1 ##1의 경우 자지 자신만 허용

    while True:
        depth += 1
        node = node_dict[p_id]

        if depth > node[3]:
            return False

        if node[1] == -1: ##제일 위의 노드까지 탐색 완료
            return True 
        
        p_id = node_dict[p_id][1] ##부모의 부모


##색깔 변경 여부를 저장하면 좋을 듯ㄱ
def change_color(m_id):
    color = node_dict[m_id][2]

    bfs_list = node_dict[m_id][-1]

    while bfs_list:
        node = bfs_list.pop(0)

        node_dict[node[0]][2] = color

        node_child_list = node[-1]
        bfs_list.extend(node_child_list)

def search_color(m_id):
    return node_dict[m_id][2]


##위의 색깔 변경 때문에 bfs로 가는 게 좋을 듯
def get_color_range(m_id):
    pass

def search_score(m_id):
    total_score = 0

    bfs_list = node_dict[m_id][-1]

    while bfs_list:
        score = get_color_range(m_id)