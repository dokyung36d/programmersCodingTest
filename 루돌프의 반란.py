import sys
import copy

N, M, P, C, D = map(int, sys.stdin.readline().split())
deer_row, deer_col = map(int, sys.stdin.readline().split())
deer_row -= 1
deer_col -= 1

matrix = [[0 for _ in range(N)] for _ in range(N)]
matrix[deer_row][deer_col] = "d"

santa_list = []
santa_score_list = [0] * P
santa_blecked_out = [0] * P

for _ in range(P):
    santa_unique_num, santa_row, santa_col = map(int, sys.stdin.readline().split())
    # santa_unique_num -= 1
    santa_row -= 1
    santa_col -= 1

    santa_list.append((santa_unique_num, santa_row, santa_col))
    matrix[santa_row][santa_col] = santa_unique_num

santa_list.sort()

def deer(pos, closest_santa_pos):
    ##최소 거리의 산타를 input으로 넣어줘야 할 듯. 최적화를 위해
    direction = (closest_santa_pos[0] - pos[0], closest_santa_pos[1] - pos[1])

    if direction[0] > 0:
        delta_r = 1
    if direction[0] == 0:
        delta_r = 0
    if direction[0] < 0:
        delta_r = -1

    if direction[1] > 0:
        delta_c = 1
    if direction[1] == 0:
        delta_c = 0
    if direction[1] < 0:
        delta_c = -1

    return (pos[0] + delta_r, pos[1] + delta_c), (delta_r, delta_c)




def santa(pos, deer_pos):
    global matrix
    # min_distance = 10 ** 10
    move_candidate = []
    direction = (deer_pos[0] - pos[0], deer_pos[1] - pos[1])
    distance_standard = calculate_distance(pos, deer_pos)
    # print(pos, deer_pos)

    if direction[0] > 0:
        moved_position = (pos[0] + 1, pos[1])
        distance = calculate_distance(moved_position, deer_pos)

        if check_index(moved_position) and matrix[moved_position[0]][moved_position[1]] in [0, "d"] and distance < distance_standard:
            move_candidate.append((distance, 3, moved_position, (1, 0)))

    if direction[0] < 0:
        moved_position = (pos[0] - 1, pos[1])
        distance = calculate_distance(moved_position, deer_pos)

        if check_index(moved_position) and matrix[moved_position[0]][moved_position[1]] in [0, "d"] and distance < distance_standard:
            move_candidate.append((distance, 1, moved_position, (-1, 0)))


    if direction[1] > 0:
        moved_position = (pos[0], pos[1] + 1)
        distance = calculate_distance(moved_position, deer_pos)

        if check_index(moved_position) and matrix[moved_position[0]][moved_position[1]] in [0, "d"] and distance < distance_standard:
            move_candidate.append((distance, 2, moved_position, (0, 1)))

    if direction[1] < 0:
        moved_position = (pos[0], pos[1] - 1)
        distance = calculate_distance(moved_position, deer_pos)

        if check_index(moved_position) and matrix[moved_position[0]][moved_position[1]] in [0, "d"] and distance < distance_standard:
            move_candidate.append((distance, 4, moved_position, (0, -1)))


    move_candidate.sort()

    if len(move_candidate) == 0: ##이동 가능한 경우가 없는 경우
        return distance_standard, pos, (0, 0)
    return move_candidate[0][0], move_candidate[0][2], move_candidate[0][3]

def collosion_by_deer(pos, direction):
    global C, D, santa_score_list, matrix
    # print(direction)
    santa_unique_num = matrix[pos[0]][pos[1]]


    santa_blecked_out[santa_unique_num - 1] = 2


    delta = (C * direction[0], C * direction[1])
    santa_score_list[santa_unique_num - 1] += C

    santa_pos = (pos[0] + delta[0], pos[1] + delta[1])

    if not check_index(santa_pos): ##matrix 밖으로 나가는 경우
        remove_santa_by_unique_num(santa_unique_num)
        matrix[pos[0]][pos[1]] = "d"
        return matrix

    if matrix[santa_pos[0]][santa_pos[1]] != 0:
        interact(santa_pos, direction)


    matrix = update_map(pos, (pos[0] + delta[0], pos[1] + delta[1]), santa_unique_num)

    return matrix

def collosion_by_santa(pos, direction, i):
    ##부딫힌 다음 distance_list 업데이트 필요
    global C, D, santa_score_list, matrix, santa_distance_list

    santa_unique_num = matrix[pos[0] - direction[0]][pos[1] - direction[1]]
    # print("pos", pos, direction)
    # print("santa unique num", santa_unique_num)

    santa_blecked_out[santa_unique_num - 1] = 1


    delta = (-D * direction[0], -D * direction[1])
    santa_score_list[santa_unique_num - 1] += D


    if D == 1:
        santa_pos = (pos[0] - direction[0], pos[1] - direction[1])
        for i in range(len(santa_distance_list)):
            if santa_distance_list[i][0] == santa_unique_num:
                santa_distance_list[i] = (santa_unique_num, 1, N - santa_pos[0], N - santa_pos[1])
        return matrix
    santa_pos = (pos[0] + delta[0], pos[1] + delta[1])


    if not check_index(santa_pos): ##matrix 밖으로 나가는 경우
        remove_santa_by_unique_num(santa_unique_num)
        matrix[pos[0] - direction[0]][pos[1] - direction[1]] = 0
        return matrix

    if matrix[santa_pos[0]][santa_pos[1]] != 0:
        interact(santa_pos, (-direction[0], -direction[1]))

    santa_before_move_pos = (pos[0] - direction[0], pos[1] - direction[1])
    matrix = update_map(santa_before_move_pos, (pos[0] + delta[0], pos[1] + delta[1]), santa_unique_num)
    for i in range(len(santa_distance_list)):
        if santa_distance_list[i][0] == santa_unique_num:
            santa_distance_list[i] = (santa_unique_num, calculate_distance(santa_pos, deer_pos), N - santa_pos[0], N - santa_pos[1])
    return matrix

##recursion 방식으로 처리
##해당 함수는 COLLISION내부에서 사용되어야 함
##pos는 충돌 이후 도착 지점, direction은 단위 delta, collisioned_santa_unique_num은 현재 이동하고 있는 산타, 침범하는 산타
def interact(pos, direction):
    global matrix, santa_distance_list, deer_pos

    after_interact_pos = (pos[0] + direction[0], pos[1] + direction[1])

    if not check_index(after_interact_pos):
        remove_santa_by_unique_num(matrix[pos[0]][pos[1]])
        matrix[pos[0]][pos[1]] = 0
        return matrix

    if matrix[after_interact_pos[0]][after_interact_pos[1]] != 0:
        ##연쇄적으로 이동하면 제일 뒤에 있는 것이 먼저 움직여야 함
        interact(after_interact_pos, direction)

    santa_unique_num = matrix[after_interact_pos[0]][after_interact_pos[1]]



    update_map(pos, (pos[0] + direction[0], pos[1] + direction[1]), matrix[pos[0]][pos[1]])
    for j in range(len(santa_distance_list)):
        if santa_distance_list[j][0] == santa_unique_num:
            santa_distance_list[j] = (santa_unique_num, calculate_distance(after_interact_pos, deer_pos), N - after_interact_pos[0], N - after_interact_pos[1])


# def get_closest_santa(santa_list, santa_distance_list):
#     min_distancee = 10 ** 10
#
#
#     for i in range(len(santa_list)):
#         if santa_distance_list[i] < min_distancee:
#             min_distancee = santa_distance_list[i]
#             santa_pos = santa_list[i]
#
#         elif santa_distance_list[i] == min_distancee:
#             if santa_distance_list[i][0] > santa_pos[0]:
#

##산타 기절하는 경우 고려
def update_map(origin_pos, moved_pos, value):
    global matrix, santa_distance_list, deer_pos

    matrix[origin_pos[0]][origin_pos[1]] = 0
    matrix[moved_pos[0]][moved_pos[1]] = value
    distance = calculate_distance(deer_pos, moved_pos)

    for i in range(len(santa_distance_list)):
        if santa_distance_list[i][0] == value:
            santa_distance_list[i] = (value, distance, N - moved_pos[0], N - moved_pos[1])

    return matrix

def calculate_distance(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2


def check_index(pos):
    if pos[0] < 0 or pos[0] >= N or pos[1] < 0 or pos[1] >= N:
        return False
    return True

def remove_santa_by_unique_num(unique_num):
    global P, santa_distance_list

    for i in range(len(santa_distance_list)):
        if santa_distance_list[i][0] == unique_num:
            santa_distance_list[i] = (unique_num, -1, -1, -1)
            break

def remove_outed_santa(santa_dist_list):
    for i in range(len(santa_dist_list) - 1, -1, -1):
        if santa_dist_list[i][2] == -1:
            santa_dist_list.pop(i)
    return santa_dist_list

if __name__ == "__main__":
    ##map의 각 point에는 "d"와 santa의 고유번호 저장
    santa_distance_list = [(i + 1, (calculate_distance((deer_row, deer_col), santa_list[i][1:])), N - santa_list[i][1], N - santa_list[i][2]) for i in range(len(santa_list))]
    ##(거리, N - 행, N - 열, 기절 여부, santa 고유번호)
    deer_pos = (deer_row, deer_col)
    # for matrix_row in matrix:
    #     print(matrix_row)
    # print()


    for _ in range(M):
        prev_deer_pos = (deer_pos[0], deer_pos[1])

        santa_distance_list.sort(key = lambda x: x[1:])
        # print(santa_distance_list)

        if not santa_distance_list:
            break



        deer_pos, deer_direction = deer(prev_deer_pos, (N - santa_distance_list[0][2], N - santa_distance_list[0][3]))

        if matrix[deer_pos[0]][deer_pos[1]] != 0:
            collosion_by_deer(deer_pos, deer_direction)


        # print(deer_pos)
        update_map(prev_deer_pos, deer_pos, "d") ##deer_row, deer_col은 이전 사슴 위치
        santa_distance_list.sort()
        # print(santa_distance_list)

        # for matrix_row in matrix:
        #     print(matrix_row)
        # print()

        for i in range(len(santa_distance_list)):
            if santa_blecked_out[santa_distance_list[i][0] - 1] != 0:
                santa_blecked_out[santa_distance_list[i][0] - 1] -= 1

                if check_index((N - santa_distance_list[i][2], N - santa_distance_list[i][3])):
                    santa_distance_list[i] = (santa_distance_list[i][0], calculate_distance((N - santa_distance_list[i][2], N - santa_distance_list[i][3]), deer_pos), santa_distance_list[i][2], santa_distance_list[i][3])
                continue

            # print(santa_distance_list[i])
            # print(matrix)
            santa_position = (N - santa_distance_list[i][2], N - santa_distance_list[i][3])
            distance, santa_pos, santa_direction = santa(santa_position, deer_pos)

            if santa_direction == (0, 0):
                santa_distance_list[i] = (santa_distance_list[i][0], distance, N - santa_pos[0], N - santa_pos[1])
            elif santa_pos == deer_pos: #collosion이 발생한 이후
                collosion_by_santa(santa_pos, santa_direction, i) ##collosion 이후의 distance_list 업데이트 필요
            else:
                update_map(santa_position, santa_pos, santa_distance_list[i][0])
                santa_distance_list[i] = (santa_distance_list[i][0], distance, N - santa_pos[0], N - santa_pos[1])

            # for matrix_row in matrix:
            #     print(matrix_row)
            # print()
        santa_distance_list = remove_outed_santa(santa_distance_list)

        for j in range(len(santa_distance_list)):
            santa_score_list[santa_distance_list[j][0] - 1] += 1

        before_matrix = copy.deepcopy(matrix)

        # print()
        # print(santa_score_list)

        # print(deer_direction)
        # deer_pos = deer((deer_row, deer_col), santa_list[])

    for i in range(len(santa_score_list)):
        print(santa_score_list[i], end= " ")