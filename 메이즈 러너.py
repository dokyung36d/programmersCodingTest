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


def rotate_rectangle(rectangle):
    num = len(rectangle)

    return_array = [[0 for _ in range(num)] for _ in range(num)]

    center_point = (num / 2, num / 2)
    
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


if __name__ == "__main__":
    array = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    print(rotate_rectangle(array))