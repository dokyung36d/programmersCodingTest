##총 9 * 3 경우 가능

from collections import deque
import sys
import copy

K,M = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(5):
    new_list = list(map(int, sys.stdin.readline().split()))
    matrix.append(new_list)

replace_list = list(map(int, sys.stdin.readline().split()))

def rotate_all_case(matrix):
    best_stadard = [360, (6, 6)]
    best_score = 0
    best_result = []

    rotate_degree_list = [90, 180, 270]
    for i in range(1, 4):
        for j in range(1, 4):
            for rotate_degree in rotate_degree_list:
                rotated_matrix = rotate(matrix, rotate_degree, (i, j))
                result = bfs(rotated_matrix)
                score = len(result)
                if score > best_score:
                    best_score = score
                    best_result = result
                    best_stadard = [rotate_degree, (i, j)]

                elif score == best_score:
                    standard = [rotate_degree, (i, j)]
                    if check_standard(best_stadard, standard):
                        best_stadard = standard
                        best_result = result

    return best_result

def check_standard(standard0, standard1):
    if standard0[0] < standard1[0]:
        return 0

    if standard0[0] > standard1[0]:
        return 1


    if standard0[1][1] < standard1[1][1]:
        return 0

    if standard0[1][1] > standard1[1][1]:
        return 1


    if standard0[1][0] < standard1[1][0]:
        return 0

    if standard0[1][0] > standard1[1][0]:
        return 1





def rotate(matrix, degree, center):
    return_matrix = copy.deepcopy(matrix)
    num_rotate = degree // 90

    edge_list = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    not_edge_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(4):
        original_index = i
        rotated_index = (i + num_rotate) % 4

        edge_point = (center[0] + edge_list[i][0], center[1] + edge_list[i][1])
        not_edge_point = (center[0] + not_edge_list[i][0], center[1] + not_edge_list[i][1])

        rotated_edge_point = (center[0] + edge_list[rotated_index][0], center[1] + edge_list[rotated_index][1])
        rotated_not_edge_point = (center[0] + not_edge_list[rotated_index][0], center[1] + not_edge_list[rotated_index][1])

        return_matrix[rotated_edge_point[0]][rotated_edge_point[1]] = matrix[edge_point[0]][edge_point[1]]
        return_matrix[rotated_not_edge_point[0]][rotated_not_edge_point[1]] = matrix[not_edge_point[0]][not_edge_point[1]]


    return_matrix[center[0]][center[1]] = matrix[center[0]][center[1]]

    return return_matrix

def bfs(matrix):
    # score = 0
    return_list = []
    visited = []

    for i in range(5):
        for j in range(5):
            if (i, j) in visited:
                continue

            result = search((i, j), matrix)
            visited.extend(result)

            if len(result) >= 3:
                return_list.extend(result)
                # score += len(result)

    return return_list

def search(start_index, matrix):
    value = matrix[start_index[0]][start_index[1]]
    delta_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    return_list = [start_index]

    d = deque([start_index])
    while d:
        current = d.popleft()

        for delta in delta_list:
            neighbors = (current[0] + delta[0], current[1] + delta[1])

            if not check_index(neighbors):
                continue

            if neighbors in return_list:
                continue

            if matrix[neighbors[0]][neighbors[1]] != value:
                continue

            return_list.append(neighbors)
            d.append(neighbors)

    return return_list

def check_index(index):
    if index[0] < 0 or index[0] >= 5 or index[1] < 0 or index[1] >= 5:
        return False
    return True

def sort(index_list):
    index_list = [(index[1], 9 - index[0]) for index in index_list]
    index_list.sort()
    index_list = [(9 - index[1], index[0]) for index in index_list]

    return index_list


if __name__ == "__main__":
    total_score = 0

    # while True:
    #     # #matrix = [[7,6,7], [7,1,5], [6,3,2]]
    #     # rotated_matrix = rotate(matrix, 90, (2, 2))
    #     # result = bfs(rotated_matrix)

    result = rotate_all_case(matrix)
    print(result)
    total_score += len(result)

    # result = search((0, 1), rotated_matrix)
    result = sort(result)
    for i in range(len(result)):
        matrix[result[i][0]][result[i][1]] = replace_list[i]
    replace_list = replace_list[len(result):]

    print(result)