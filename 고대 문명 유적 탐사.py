##총 9 * 3 경우 가능

from collections import deque


def rotate(matrix, degree):
    return_matrix = [[0 for _ in range(3)] for _ in range(3)]
    center = (1, 1)
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
    visited = []

    for i in range(5):
        for j in range(5):
            if (i, j) in visited:
                continue

def search(start_index, matrix):
    value = matrix[start_index[0]][start_index[1]]
    delta_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    return_list = []

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
    if index[0] < 0 or index[0] > 5 or index[1] < 0 or index[1] > 5:
        return False
    return True


if __name__ == "__main__":
    matrix = [[7,6,7], [7,1,5], [6,3,2]]
    rotated_matrix = rotate(matrix, 90)
    result = search((0, 1), rotated_matrix)

    print(result)