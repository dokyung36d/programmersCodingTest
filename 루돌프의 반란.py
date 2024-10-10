import sys

N, M, P, C, D = map(int, sys.stdin.readline().split())
deer_row, deer_col = map(int, sys.stdin.readline().split())
deer_row -= 1
deer_col -= 1

matrix = [[0 for _ in range(N)] for _ in range(N)]
matrix[deer_row][deer_col] = "d"

santa_list = []
santa_score_list = [0] * P

for _ in range(P):
    santa_unique_num, santa_row, santa_col = map(int, sys.stdin.readline().split())
    santa_unique_num -= 1
    santa_row -= 1
    santa_col -= 1

    santa_list.append((santa_row, santa_col))
    matrix[santa_row][santa_col] = santa_unique_num

def deer(pos, closest_santa_pos):
    ##최소 거리의 산타를 input으로 넣어줘야 할 듯. 최적화를 위해
    direction = (closest_santa_pos[0] - pos[0], closest_santa_pos[1] - pos[0])

    if direction[0] > 0:
        delta_r = -1
    if direction[0] == 0:
        delta_r = 0
    if direction[0] < 0:
        delta_r = 1

    if direction[1] > 0:
        delta_c = 1
    if direction[1] == 0:
        delta_c = 0
    if direction[1] < 0:
        delta_c = -1

    return (pos[0] + delta_r, pos[1] + delta_c)




def santa(pos, deer_pos):
    min_distance = 10 ** 10
    move_candidate = []
    direction = (deer_pos[0] - pos[0], deer_pos[1] - pos[1])

    if direction[0] > 0:
        moved_position = (pos[0] - 1, pos[1])
        distance = calculate_distance(moved_position, deer_pos)
        if distance < min_distance:
            min_distance = distance
            santa_pos = moved_position

    if direction[0] < 0:
        moved_position = (pos[0] + 1, pos[1])
        if distance < min_distance:
            min_distance = distance
            santa_pos = moved_position


    if direction[1] > 0:
        moved_position = (pos[0], pos[1] + 1)
        if distance < min_distance:
            min_distance = distance
            santa_pos = moved_position

    if direction[1] < 0:
        moved_position = (pos[0], pos[1] - 1)
        if distance < min_distance:
            min_distance = distance
            santa_pos = moved_position


    return min_distance, santa_pos

def collosion(pos, direction, is_deer_moved : bool, santa_unique_num):
    global C, D

    if is_deer_moved:
        delta = (C * direction[0], C * direction[1])
        santa_score_list[santa_unique_num - 1] += C
        matrix = update_map(pos, (pos[0] + delta[0], pos[1] + delta[1], "s"))

    else:
        delta = (D * direction[0], D * direction[1])
        santa_score_list[santa_unique_num - 1] += D
        matrix = update_map(pos, (pos[0] + delta[0], pos[1] + delta[1], "s"))

    return matrix

def interact(pos, direction, collosioned_santa_value):
    matrix = update_map(pos, (pos[0] + direction[0], pos[1] + direction[1]), matrix[pos[0]][pos[1]])
    matrix[pos[0]][pos[1]] = collosioned_santa_value

    return matrix

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
    matrix[origin_pos[0]][origin_pos[1]] = 0
    matrix[moved_pos[0]][moved_pos[1]] = value

    return matrix

def calculate_distance(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2


def check_index(pos):
    if pos[0] < 0 or pos[0] >= N or pos[1] < 0 or pos[1] >= N:
        return False
    return True

if __name__ == "__main__":
    ##map의 각 point에는 "d"와 santa의 고유번호 저장
    santa_distance_list = [(calculate_distance((deer_row, deer_col), santa_list[i]), N - santa_list[i][0], N - santa_list[i][1], i) for i in range(len(santa_list))]
    ##(거리, N - 행, N - 열, santa 고유번호)
    santa_distance_list.sort()

    print(santa_distance_list)
    # deer_pos = deer((deer_row, deer_col), santa_list[])