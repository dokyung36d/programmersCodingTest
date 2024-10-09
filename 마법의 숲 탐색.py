import sys
import copy

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
    second_delta_list = [(-1, -1), (0, -2), (1, -2), (1, -1), (2, -1)]
    second_result = moved_position_available(current_pos, second_delta_list, map)

    if second_result == 0:
        moved_pos = (current_pos[0] + 1, current_pos[1] - 1)
        return 1, moved_pos ##mean down is possible


    ##Third, Check Third Case
    third_delta_list = [(-1, 1), (0, 2), (1, 2), (1, 1), (2, 1)]
    third_result = moved_position_available(current_pos, third_delta_list, map)

    if third_result == 0:
        moved_pos = (current_pos[0] + 1, current_pos[1] + 1)
        return 2, moved_pos ##mean down is possible

    return -1, (0, 0)


def moved_position_available(pos, delta_list, map):
    global R, C

    flag = 0
    for delta in delta_list:
        moved_x_pos, moved_y_pos = pos[0] + delta[0], pos[1] + delta[1]
        if moved_x_pos >= R or moved_y_pos < 0 or moved_y_pos >= C:
            ##처음 시작할 때 index문제로 전체 박스의 Row갯수를 + 3 해야할 듯
            flag = 1
            break

        if map[moved_x_pos][moved_y_pos][0] == 1: ##이미 있는 경우
            flag = 1
            break

    return flag

def check_golem_in_box(pos):
    if pos[0] <= 3:
        return False
    return True

def golem(start_col, direction, map):
    ##여기서는 이동만, 더 이상 움직일 수 없을 때 골렘에서 내려서 하는 것은 다른 함수에서
    pos = (1, start_col)

    while True:
        next_move, moved_pos = get_next_move(pos, map)
        # print("next move", next_move)

        if next_move == -1: ##move is not available
            return pos, direction

        changed_direction = rotate(next_move, direction)

        pos = moved_pos
        direction = changed_direction

    return pos, direction

def clear_map(map):
    global R, C
    ##지도 0 : 비어 있음, 1:차지하고 있는 공간
    ##각 지도 맵마다 골렘 고유번호도 넣어야 할 듯(다른 골렘일 경우에만 넘어갈 수 있도록)
    for i in range(3, R):
        for j in range(C):
            map[i][j] = [0, -1, None, None] ##상태, Golem 고유번호, 센터, direction

    return map


def apply_to_map(moved_pos, direction, golem_unique_num, map):
    delta_list = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]

    for delta in delta_list:
        ##상태, Golem 고유번호, 센터, direction
        moved_pos_x, moved_pos_y = moved_pos[0] + delta[0], moved_pos[1] + delta[1]
        map[moved_pos_x][moved_pos_y] = (1, golem_unique_num, moved_pos, direction)

    # direction_pos_x, direction_pos_y = moved_pos[0] + direction[0], moved_pos[1] + direction[1]
    # map[direction_pos_x][direction_pos_y] = (golem_unique_num, 2)

    return map

#dfs로 가야할 듯
def calculate_score(pos, direction, map, visited):
    global R
    best_score = pos[0] + 1 ##센터에서 한 칸 아래가 현재 최대
    ##영역 확장할 때 golem_unique_num을 이용해 무한 loop 방지
    ##아니면 map에 정보를 넣을 때 부터 max_row를 넣어도 될 듯, 반복된 계산을 줄일 수 있음 -> 반례 존재

    if best_score == R:
        return best_score

    jump_points = get_jump_points(pos, direction, map, visited) ##문제 없음
    # print(jump_points)

    ##visited 활용하기
    for jump_point in jump_points:
        if jump_point[0] in visited:
            continue

        new_score = jump_point[1][0] + 1
        if new_score > best_score:
            best_score = new_score

        new_score = calculate_score(jump_point[1], jump_point[2], map, visited + [jump_point[0]])
        if new_score > best_score:
            best_score = new_score

        if best_score == R:
            break

    return best_score


##매 회마다 하는 것보다는 각 영역마다 최종 값을 저장하는 게 효율이 좋을 듯
##구한 이후에 새로 내려운 골렘이 다른 값에 영향을 미치면 그것도 업데이트해야 할 듯
##아이디어 자체는 기존과 비슷한 듯
def get_jump_points(pos, direction, map, visited):
    ##jump 이후의 center과 direction을 return 함
    jump_points = []
    jump_start_pos = (pos[0] + direction[0], pos[1] + direction[1])
    reverse_direction = (-direction[0], -direction[1])

    delta_list = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    delta_list.remove(reverse_direction)

    for delta in delta_list:
        jumped_x, jumped_y = jump_start_pos[0] + delta[0], jump_start_pos[1] + delta[1]

        if jumped_x < 0 or jumped_x >= R or jumped_y < 0 or jumped_y >= C:
            continue

        if map[jumped_x][jumped_y][0] != 0 and map[jumped_x][jumped_y][1] not in visited:
            ##점프한 곳이 비어있지 않고 이전에 방문한 골렘이 아닌 경우

            jump_point_center, jump_point_direction = map[jumped_x][jumped_y][2], map[jumped_x][jumped_y][3]
            jump_golem_unique_number = map[jumped_x][jumped_y][1]
            jump_points.append((jump_golem_unique_number, jump_point_center, jump_point_direction))

    return jump_points





if __name__ == "__main__":
    delta_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    map = [[(0, -1, None, None) for _ in range(C)] for _ in range(R)]
    original_map = copy.deepcopy(map)
    ##상태, Golem 고유번호, 센터, direction

    total_score = 0

    for i in range(K):
        pos, direction = golem(golem_infos[i][0] - 1, delta_list[golem_infos[i][1]], map)

        if not check_golem_in_box(pos):
            map = original_map
            original_map = copy.deepcopy(map)
            pos, direction = golem(golem_infos[i][0], delta_list[golem_infos[i][1]], map)
            continue

        map = apply_to_map(pos, direction, i, map)
        score = calculate_score(pos, direction, map, [i]) - 2

        # print(pos)
        # print("direction", direction)
        # print(score)
        total_score += score

    print(total_score)