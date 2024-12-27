import sys
from collections import defaultdict

def solution():
    R, C = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(R):
        newString = sys.stdin.readline()
        newString = newString[:-1]
        newRow = []

        for j in range(C):
            newRow.append(newString[j])

        matrix.append(newRow)

    
    
    return dfs((0, 0), [matrix[0][0]], matrix)

def dfs(pos, visited, matrix):
    maxNumVisited = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    flag = 0

    for direction in directions:
        movedPos = addTwoTuple(pos, direction)
        if not checkIndex(movedPos, len(matrix), len(matrix[0])):
            continue

        newAlphabet = matrix[movedPos[0]][movedPos[1]]
        if newAlphabet in visited:
            continue

        flag = 1
        result = dfs(movedPos, visited + [newAlphabet], matrix)
        if result >= maxNumVisited:
            maxNumVisited = result

    if flag == 0:
        return len(visited)
    
    return maxNumVisited


def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def checkIndex(pos, R, C):
    if 0 <= pos[0] < R and 0 <= pos[1] < C:
        return True
    
    return False


print(solution())