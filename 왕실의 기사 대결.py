##체스판의 크기가 그렇게 크지 않으므로 전체 탐색으로 해도 괜찮을 듯

import sys

sys.setrecursionlimit(10**6)

L, N ,Q = map(int, input().split())

total_damage = 0

map_matrix = []
fighter_info_list = []
command_list = []
trap_list = []
wall_list = []

for i in range(L):
    map_matrix.append(list(map(int, input().split())))

    for j in range(L):
        if map_matrix[i][j] == 1:
            trap_list.append((i, j))

    for j in range(L):
        if map_matrix[i][j] == 2:
            wall_list.append((i, j))

for _ in range(N):
    fighter_info_list.append(list(map(int, input().split())))

    fighter_info_list[-1][0] -= 1
    fighter_info_list[-1][1] -= 1


#기사가 아웃되었는지 여부
fighter_outed =[0] * N

def check_move_available(edge, height, width):
    global trap_list
    ##맵 밖의 벽에 막힌 경우
    if edge[0] < 0 or edge[0] + height > L or edge[1] < 0 or edge[1] + width > L:
        return False
    
    for i in range(len(wall_list)):
        if edge[0] <= wall_list[i][0] < edge[0] + height and  edge[1] <= wall_list[i][1] < edge[1] + width:
            return False


    # for i in range(len(fighter_info_list)):
    #     fighter_edges = get_four_edge(fighter_info_list[0:2], fighter_info_list[2], fighter_info_list[3])

    #     for fighter_edge in fighter_edges:
    #         if edge[0] <= fighter_edge[i][0] <= edge[0] + height and  edge[1] <= fighter_edge[i][1] <= edge[1] + width:
    #             return False
        
    return True


def change_fighter_position(fighter_index, edge, direction_index):
    global map_matrix, total_damage

    height, width = fighter_info_list[fighter_index][2], fighter_info_list[fighter_index][3]
    
    direction_dict = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)}

    direction  = direction_dict[direction_index]

    moved_edge = (edge[0] + direction[0], edge[1] + direction[1])

    if not check_move_available: ##제일 끝에 있는 것이 이동 불가능하면 모두 이동 불가능함.
        return False
    
    counter_fighter_list = check_fight_avail(moved_edge, height, width, fighter_index)
    

    if not counter_fighter_list: ##이동한 자리애 상대방 기사가 없는 경우
        damage = get_damage(moved_edge, height, width)

        total_damage += damage
        remain_health = fighter_info_list[fighter_index][-1] - damage

        fighter_info_list[fighter_index] = (moved_edge[0], moved_edge[1], height, width, remain_health)

        if remain_health <= 0:
            fighter_outed[fighter_index] = 1

        return True
    

    # result = change_fighter_position(counter_fighter_index, moved_edge, height = height, width = width)
    for counter_fighter_index in counter_fighter_list:
        counter_fighter_edge = (fighter_info_list[counter_fighter_index][0], fighter_info_list[counter_fighter_index][1])
        result = change_fighter_position(counter_fighter_index, counter_fighter_edge, direction_index)

        if result == False:
            return False
    
    fighter_info_list[fighter_index] = (moved_edge[0], moved_edge[1], height, width, fighter_info_list[fighter_index][-1])
    return True
    



def check_fight_avail(moved_edge, height, width, fighter_index): ##이동한 위치에 기존 기사가 존재하는 지 check
    fighter_avail_list = []
    for i in range(len(fighter_info_list)):
        if fighter_outed[i] == 1 or fighter_index == i: ##이미 아웃된 경우, 자기 자신인 경우
            continue


        fighter_edges = get_four_edge(fighter_info_list[i][0:2], fighter_info_list[i][2], fighter_info_list[i][3])

        for fighter_edge in fighter_edges:
            if moved_edge[0] <= fighter_edge[0] < moved_edge[0] + height and  moved_edge[1] <= fighter_edge[1] < moved_edge[1] + width:
                fighter_avail_list.append(i)
    
    return fighter_avail_list ##이동한 자리에 기사가 없어 싸움이 필요없는 경우

def get_damage(edge, height, width):
    global trap_list

    total_damage = 0

    for trap in trap_list:
        if edge[0] <= trap[0] < edge[0] + height and edge[1] <= trap[1] < edge[1] + width:
            total_damage += 1

    return total_damage


def get_four_edge(edge, height, width):
    edges = [(edge[0], edge[1]), (edge[0] + height, edge[1]), (edge[0], edge[1] + width), (edge[0] + height, edge[1] + width)]

    return edges


for _ in range(Q):
    fighter_index, direction_index = map(int, input().split())
    fighter_index -= 1

    if fighter_outed[fighter_index] == 1:
        continue

    edge = (fighter_info_list[fighter_index][0], fighter_info_list[fighter_index][1])
 
    result = change_fighter_position(fighter_index, edge, direction_index)

print(total_damage)
