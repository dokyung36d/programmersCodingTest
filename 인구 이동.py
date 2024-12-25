import sys

def solution():
    N, L, R = map(int, sys.stdin.readline().split())

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        newRow = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            matrix[i][j] = newRow[j]
    
    answer = 0

    while True:
        matrix, peopleMoveFlag = getTurnResult(matrix, N, L, R)
        # for row in matrix:
        #     print(row)
        # print()
        if peopleMoveFlag == 0:
            break

        answer += 1

    return answer

def getTurnResult(matrix, N, L, R):
    peopleMoveFlag = 0

    visitedMatrix = [[0 for _ in range(N)] for _ in range(N)]
    indexList = [(i, j) for i in range(N) for j in range(N)]
    while indexList:
        currentIndex = indexList.pop()
        if visitedMatrix[currentIndex[0]][currentIndex[1]] == 1:
            continue

        visitedMatrix[currentIndex[0]][currentIndex[1]] = 1
        matrix, visitedMatrix, flag = bfs(matrix, currentIndex, visitedMatrix, N, L, R)

        if flag == 1:
            peopleMoveFlag = 1

    return matrix, peopleMoveFlag


def bfs(matrix, currentPos, visitedMatrix, N, L, R):
    # maxVisited = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    peopleMoveFlag = 0

    queue = [currentPos]
    movedPosList = [currentPos]
    while queue:
        currentPos = queue.pop()

        for direction in directions:
            movedPos = addTwoTuple(currentPos, direction)
            if not checkIndex(movedPos, N):
                continue

            if not checkWhetherMoveAvailable(matrix, currentPos, movedPos, L, R):
                continue

            if movedPos in movedPosList:
                continue

            if visitedMatrix[movedPos[0]][movedPos[1]] == 1:
                continue

            visitedMatrix[movedPos[0]][movedPos[1]] = 1
            peopleMoveFlag = 1
            queue.append(movedPos)
            movedPosList.append(movedPos)

            # if len(updatedVisited) > len(maxVisited):
            #     maxVisited = updatedVisited
    # for movedPos in movedPosList:
    #     visitedMatrix[movedPos[0]][movedPos[1]] = 1


    if peopleMoveFlag == 0:
        return matrix, visitedMatrix, peopleMoveFlag


    totalPeople = 0
    for visitedIndex in movedPosList:
        totalPeople += matrix[visitedIndex[0]][visitedIndex[1]]

    meanPeople = totalPeople // len(movedPosList)
    for visitedIndex in movedPosList:
        matrix[visitedIndex[0]][visitedIndex[1]] = meanPeople
    return matrix, visitedMatrix, peopleMoveFlag


def checkWhetherMoveAvailable(matrix, index1, index2, L, R):
    value1, value2 = matrix[index1[0]][index1[1]], matrix[index2[0]][index2[1]]

    if L <= abs(value1 - value2) <= R:
        return True
    
    return False


def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def checkIndex(index, N):
    if 0 <= index[0] < N and 0 <= index[1] < N:
        return True
    
    return False



print(solution())