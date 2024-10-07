import sys

R, C, K = map(int, sys.stdin.readline().split())
R += 3 ##초기에 골렘이 들어갈 때를 고려하기 위해 (-3으로 하면 아래에 있는 행으로 가게 됨

golem_infos = []

for _ in range(K):
    column, direction = map(int, sys.stdin.readline().split())
    golem_infos.append([column, direction])

#현재 골렘의 센터에서 탈출구의 입구를 기준으로 선택
# EX) 왼쪽이 출입구 -> (0, -1)
def rotate(move, current_delta):
    delta_list = [(0, -1), (1, 0), (0, 1), (-1, 0)] ##서 남 동 북

    current_delta_index = delta_list.index(current_delta)
    if move == 0: ##그냥 아래로 내려가는 경우
        changed_delta_index = current_delta_index

    elif move == 1: ## (2) 경우 : 서쪽 방향으로 회전 하는 경우
        changed_delta_index = (current_delta_index + 1) % 4

    elif move == 2: ## (3) 경우 : 동쪽 방향으로 회전
        changed_delta_index = (current_delta_index - 1) % 4


    return delta_list[changed_delta_index]

def get_next_move(current_pos, map):
    global R, C
    ## return a possible move
    ##0 : down, 1 : left, 2 : right

    ##First, Check First Case
    first_delta_list = [(1, -1), (2, 0), (1, 1)]
    first_result = moved_position_available(current_pos, first_delta_list, map)

    if first_result == 0:
        moved_pos = (current_pos[0] + 1, current_pos[1])
        return 0, moved_pos ##mean down is possible


    ##Second, Check Second Case
    second_delta_list = [(1, -2), (1, -1), (2, -1)]
    second_result = moved_position_available(current_pos, second_delta_list, map)

    if second_result == 0:
        moved_pos = (current_pos[0] + 1, current_pos[1] - 1)
        return 1, moved_pos ##mean down is possible


    ##Third, Check Third Case
    third_delta_list = [(1, 2), (1, 1), (2, 1)]
    third_result = moved_position_available(current_pos, third_delta_list, map)

    if third_result == 0:
        moved_pos = (current_pos[0] + 1, current_pos[1] + 1)
        return 2, moved_pos ##mean down is possible

    return -1, (0, 0)


def moved_position_available(pos, delta_list, map):
    flag = 0
    for delta in delta_list:
        moved_x_pos, moved_y_pos = pos[0] + delta[0], pos[1] + delta[1]
        if moved_x_pos > R - 2 or moved_y_pos < 1 or moved_y_pos > C - 2:
            ##처음 시작할 때 index문제로 전체 박스의 Row갯수를 + 3 해야할 듯
            flag = 1
            break

        if map[moved_x_pos][moved_y_pos] == 1: ##이미 있는 경우
            flag = 1
            break

    return flag

def check_golem_in_box(pos):
    if pos[0] <= 3:
        return False
    return True

def golem(start_col, direction, map):
    ##여기서는 이동만, 더 이상 움직일 수 없을 때 골렘에서 내려서 하는 것은 다른 함수에서
    pos = (0, start_col)

    while True:
        next_move, moved_pos = get_next_move(pos, map)

        if next_move == -1: ##move is not available
            return pos

        changed_direction = rotate(next_move, direction)

        pos = moved_pos
        direction = changed_direction

    return pos, direction

def clear_map(map):
    global  R, C
    ##지도 0 : 비어 있음, 1:차지하고 있는 공간 2 : 탈출 방향
    ##각 지도 맵마다 골렘 고유번호도 넣어야 할 듯(다른 골렘일 경우에만 넘어갈 수 있도록)
    for i in range(3, R):
        for j in range(C):
            map[i][j] = (-1, 0) #고유 번호, 상태

    return map


def apply_to_map(moved_pos, direction, golem_unique_num, map):
    delta_list = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]

    for delta in delta_list:
        moved_pos_x, moved_pos_y = moved_pos[0] + delta[0], moved_pos[1] + delta[1]
        map[moved_pos_x][moved_pos_y] = (golem_unique_num, 1)

    direction_pos_x, direction_pos_y = moved_pos[0] + direction[0], moved_pos[1] + direction[1]
    map[direction_pos_x][direction_pos_y] = (golem_unique_num, 2)

    return map

def calculate_score(pos, direction, golem_unique_num):
    score = pos[0]

    ##영역을 확장한다는 아이디어로 Go하면 좋을 듯
    ##영역 확장할 때 golem_unique_num을 이용해 무한 loop 방지
    ##아니면 map에 정보를 넣을 때 부터 max_row를 넣어도 될 듯, 반복된 계산을 줄일 수 있음



if __name__ == "__main__":
    map = [[(-1, 0) for _ in range(C)] for _ in range(R)]

    total_score = 0

    for i in range(K):
        pos, direction = golem(golem_infos[i][0], golem_infos[i][1])

        if not check_golem_in_box(pos):
            map = clear_map()
            pos, direction = golem(golem_infos[i][0], golem_infos[i][1])

        map = apply_to_map(pos, direction)
        score = calculate_score(pos, direction, map)

        total_score += score