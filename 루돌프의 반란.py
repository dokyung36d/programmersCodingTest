import sys

N, M, P, C, D = map(int, sys.stdin.readline().split())
deer_row, deer_col = map(int, sys.stdin.readline().split())

map = [[0 for _ in range(N)] for _ in range(N)]
map[deer_row][deer_col] = "d"

santa_list = []

for _ in range(P):
    santa_num, santa_row, santa_col = map(int, sys.stdin.readline().split())

    santa_list.append((santa_row, santa_col))
    map[santa_row][santa_col] = ("s", santa_num)

def deer(pos, map):
    ##최소 거리의 산타를 input으로 넣어줘야 할 듯. 최적화를 위해
    pass

def santa(pos, deer_pos):
    min_distance = 10 ** 10
    move_candidate = []
    direction = (deer_pos[0] - pos[0], deer_pos[1] - pos[0])

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

def calculate_distance(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2

if __name__ == "__main__":
    pass