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

def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def check_move(pos):
    global map_info

    row, col = pos[0], pos[1]

    if map_info[row][col] == 0:
        return True
    
    return False

def check_in_map(pos):
    global N

    if 0 <= pos[0] < N and 0 <= pos[1] < N:
        return True

    return False 


def rotate_rectangle(rectangle):
    num = len(rectangle)

    return_array = [[0 for _ in range(num)] for _ in range(num)]

    center_point = ((num - 1) / 2, (num - 1) / 2)
    
    for i in range(num):
        for j in range(num):
            roated_row, rotated_col = rotate((i, j), center_point)


            if rectangle[i][j] != 0:
                rectangle[i][j] -= 1

            return_array[roated_row][rotated_col] = rectangle[i][j]

    return return_array

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

def get_closest_user():
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

    
    return closest_user


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



if __name__ == "__main__":
    array = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]