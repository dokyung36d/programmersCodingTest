## https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=3&pageSize=5

N, M, K = map(int, input().split())

map_info = []
user_dict = {}

for _ in range(N):
    new_list = list(map(int, input().split()))

    map_info.append(new_list)

for i in range(M):
    row, col = map(int, input().split())
    
    row -= 1
    col -= 1

    user_dict[i] = (row, col)

exit_row, exit_col = map(int, input().split())
exit_pos = (exit_row, exit_col)


## 각각 상, 하, 좌,우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def check_move(pos):
    global map_info

    row, col = pos[0], pos[1]

    ## map 밖으로 벗어난 경우
    if not check_in_map((row, col)):
        return False

    if map_info[row][col] == 0:
        return True
    
    return False

def check_in_map(pos):
    global N

    if 0 <= pos[0] < N and 0 <= pos[1] < N:
        return True

    return False 


def rotate_rectangle(rectangle, exit_standard_pos):
    num = len(rectangle)

    return_array = [[0 for _ in range(num)] for _ in range(num)]

    center_point = ((num - 1) / 2, (num - 1) / 2)
    
    for i in range(num):
        for j in range(num):
            roated_row, rotated_col = rotate((i, j), center_point)


            if rectangle[i][j] != 0:
                rectangle[i][j] -= 1

            return_array[roated_row][rotated_col] = rectangle[i][j]


    ## exit만 따로 구하기
    exit_rotated_pos = rotate(exit_standard_pos, center_point)

    return return_array, exit_rotated_pos

def rotate(point, center_point):
    standard_point = (point[0] - center_point[0], point[1] - center_point[1])

    rotated_standard_point = (standard_point[1], -standard_point[0])

    return_point = (int(rotated_standard_point[0] + center_point[0]),
                    int(rotated_standard_point[1] + center_point[1]))
    
    return return_point

def get_sub_array(array, row_start, row_end, col_start, col_end):
    return_array = []

    rows = array[row_start:row_end]

    for row in rows:
        return_array.append(row[col_start:col_end])

    return return_array

def get_smallest_rectangle():
    global user_dict, exit_row, exit_col

    exit_pos = (exit_row, exit_col)
    closest_user = -1

    best_rectangle = (50, 50, 100)

    users = list(user_dict.keys())

    for user in users:
        user_row, user_col = user_dict[user][0], user_dict[user][1]
        user_pos = (user_row, user_col)

        rectangle = make_rectangle(user_pos, exit_pos)

        ## Can not make Rectangle
        if rectangle == False:
            continue
        
        ##기존 정사각형보다 한 변의 길이가 작은 경우
        if rectangle[-1] < best_rectangle[-1]:
            best_rectangle = rectangle


        ## 기존 정사각형의 한 변의 길이와 동일한 경우
        elif rectangle[-1] == best_rectangle[-1]:
            if rectangle[0] < best_rectangle[0]:
                best_rectangle = rectangle

            elif rectangle[0] == best_rectangle[0]:
                if rectangle[1] < best_rectangle[1]:
                    best_rectangle = rectangle

    
    return best_rectangle


def make_rectangle(user_pos, exit_pos):
    global N
    assert user_pos != exit_pos

    distance = get_distance(user_pos, exit_pos)

    ## 동일한 행인 경우
    if user_pos[0] == exit_pos[0]:
        lower_row = user_pos[0] - row
        higher_row = user_pos[0] + row

        ##위로 정사각형 생성 
        if 0 <= lower_row < N:
            return (lower_row, min(user_pos[1], exit_pos[1]), distance)
        
        ##아래로 정사각형 생성
        if 0 <= higher_row < N:
            return (higher_row, min(user_pos[1], exit_pos[1]), distance)
        
        return False

    
    ## 동일한 열인 경우
    if user_pos[1] == exit_pos[1]:
        left_col = user_pos[1] - distance
        right_col = user_pos[1] + distance

        if 0 <= left_col < N:
            return (min(user_pos[0], user_pos[0]), left_col, distance)
        
        if 0 <= right_col < N:
            return (min(user_pos[0], exit_pos[0]), right_col, distance)
        
        return False

    ## 동일한 행, 열이 아닌 경우
    min_row = min(user_pos[0], user_pos[0])
    min_col = min(user_pos[1], exit_pos[1])

    ##더 큰 값이 직사각형 한 변의 길이가 됨.
    distance = max(min_row, min_col)

    if not check_in_map((min_row + distance, min_col + distance)):
        return False

    return (min_row, min_col, distance)


def move_user(user_pos, exit_pos):
    distance = get_distance(user_pos, exit_pos)

    for direction in directions:
        moved_user_pos = (user_pos[0] + direction[0], user_pos[1] + direction[1])

        if not check_move(moved_user_pos):
            continue

        moved_distance = get_distance(moved_user_pos, exit_pos)

        if moved_distance < distance:
            return moved_user_pos

    ##모든 방향으로 이동이 불가능한 경우
    return user_pos


def apply_sub_array_to_main_array(main_array, sub_array):
    pass


total_move = 0

for _ in range(K):
    for user in list(user_dict.keys()):
        user_pos = user_dict[user]

        moved_user_pos = move_user(user_pos, exit_pos)

        if user_pos != moved_user_pos:
            total_move += 1

        if moved_user_pos == exit_pos:
            del user_dict[user]
    
    
    rectangle = get_smallest_rectangle()
    row_start, col_start, distance = rectangle[0], rectangle[1], rectangle[2]

    sub_array = get_sub_array(row_start, row_start + distance, col_start, col_start + distance)
    exit_standard_pos = (exit_row - row_start, exit_col - col_start)

    rotated_sub_array, exit_rotated_pos = rotate_rectangle(sub_array, exit_standard_pos)

    exit_rotated_pos = (exit_rotated_pos[0] + row_start, exit_rotated_pos[1] + col_start)
    exit_pos = exit_rotated_pos

