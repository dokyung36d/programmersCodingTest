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

    stack = [((0, 0), [matrix[0][0]], [(0, 0)])]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitedDict = defaultdict(int)
    answer = 0

    while stack:
        node = stack.pop()
        pos, visitedAlphabets, visitedPoses = node[0], node[1], node[2]
        flag = 0

        for direction in directions:
            movedPos = addTwoTuple(pos, direction)
            if not checkIndex(movedPos, len(matrix), len(matrix[0])):
                continue

            newAlphabet = matrix[movedPos[0]][movedPos[1]]
            if newAlphabet in visitedAlphabets:
                continue

            if visitedDict[movedPos] == set(visitedAlphabets):
                continue
            
            flag = 1
            stack.append((movedPos, visitedAlphabets + [newAlphabet], visitedPoses + [movedPos]))


        if flag == 1:
            continue

        ##더 이상 진행할 수 없는 경우
        if len(visitedAlphabets) > answer:
            answer = len(visitedAlphabets)

        for i in range(1, len(visitedPoses)):
            visitedDict[visitedPoses[i]] = set(visitedAlphabets[:i])
    
    return answer



def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def checkIndex(pos, R, C):
    if 0 <= pos[0] < R and 0 <= pos[1] < C:
        return True
    
    return False


print(solution())