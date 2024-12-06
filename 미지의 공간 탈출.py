def makeTimeWallMatrix(infos, M):

    matrix = [[-1 for _ in range(3 * M)] for _ in range(3 * M)]

    ## East
    eastMatrix = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(0, M):
        newCol = infos[i]
        for j in range(M):
            eastMatrix[j][i] = newCol[M - j - 1]
    matrix = applySmallMatrixToBigMatrix(matrix, eastMatrix, M , 2 * M, M)

    ## West
    westMatrix = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M, 2 * M):
        newCol = infos[i]
        for j in range(M):
            westMatrix[M - j - 1][2 * M - i - 1] = newCol[M - j - 1]
    matrix = applySmallMatrixToBigMatrix(matrix, westMatrix, M, 0, M)

    ## South
    southMatrix = []
    for i in range(2 * M, 3 * M):
        southMatrix.append(infos[i])
    matrix = applySmallMatrixToBigMatrix(matrix, southMatrix, 2 * M, M, M)

    ## North
    northMatrix = []
    for i in range(3 * M, 4 * M):
        northMatrix.insert(0, infos[i][::-1])

    matrix = applySmallMatrixToBigMatrix(matrix, northMatrix, 0, M, M)

    ## Center
    centerMatrix = []
    for i in range(4 * M, 5 * M):
        centerMatrix.append(infos[i])

        for j in range(len(infos[i])):
            if infos[i][j] == 2:
                startPoint = (i - 4 * M, j)
    matrix = applySmallMatrixToBigMatrix(matrix, centerMatrix, M, M, M)

    
    return matrix, startPoint
    

def applySmallMatrixToBigMatrix(bigMatrix, smallMatrix, rowStart, ColStart, M):

    for i in range(M):
        for j in range(M):
            row, col = rowStart + i, ColStart + j

            bigMatrix[row][col] = smallMatrix[i][j]

    return bigMatrix

def bfsInTimeWall(startPoint, dest, timeWallMatrix, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitedMatrix = [[0 for _ in range(3 * M)] for _ in range(3 * M)]
    visitedMatrix[startPoint[0]][startPoint[1]] = 1

    queue = [(startPoint, 0)]

    while queue:
        node = queue.pop(0)
        pos, depth = node[0], node[1]

        for i in range(4):
            direction = directions[i]
            
            if not checkIndexInTimeWallMatrix((pos[0] + direction[0], pos[1] + direction[1]), M):
                continue

            movedPos = moveInTimeWall(pos, direction, timeWallMatrix, M)

            if timeWallMatrix[movedPos[0]][movedPos[1]] == 1:
                continue

            if visitedMatrix[movedPos[0]][movedPos[1]] != 0:
                continue

            if movedPos == dest:
                return depth + 1
            
            visitedMatrix[movedPos[0]][movedPos[1]] = 1
            newNode = (movedPos, depth + 1)
            queue.append(newNode)

    return -1



def moveInTimeWall(pos, direction, timeWallMatrix, M):
    
    movedPos = (pos[0] + direction[0], pos[1] + direction[1])

    if timeWallMatrix[movedPos[0]][movedPos[1]] != -1:
        return movedPos
    

    ## 2, 4 사분면에 존재하는 경우
    if checkDiagonalInTimeWallMatrix(movedPos, M):
        return (pos[1], pos[0])
    
    return (3 * M - pos[1] - 1, 3 * M - pos[0] - 1)
    


def checkDiagonalInTimeWallMatrix(pos, M):
    if 0 <= pos[0] < M and 0 <= pos[1] < M:
        return True
    
    if 2 * M <= pos[0] < 3 * M and 2 * M <= pos[1] < 3 * M:
        return True
    
    return False

def checkIndexInTimeWallMatrix(pos, M):

    if 0 <= pos[0] < 3 * M and 0 <= pos[1] < 3 * M:
        return True
    
    return False

def bfsIn2d(startPos, dest, mapMatrix, depth, spreads):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visitedMatrix = [[0 for _ in range(len(mapMatrix))] for _ in range(len(mapMatrix))]
    visitedMatrix[startPos[0]][startPos[1]] = 1

    queue = [(startPos, depth, [startPos])]

    while queue:
        node = queue.pop(0)
        pos, depth, visited = node[0], node[1], node[2]

        for direction in directions:
            movedPos = (pos[0] + direction[0], pos[1] + direction[1])

            if not checkIndexInMapMatrix(movedPos, len(mapMatrix)):
                continue

            if visitedMatrix[movedPos[0]][movedPos[1]] == 1:
                continue

            if mapMatrix[movedPos[0]][movedPos[1]] == 1 or mapMatrix[movedPos[0]][movedPos[1]] == 3:
                continue

            if movedPos == dest:
                return depth + 1, visited
            
            if not checkSpreads(movedPos, depth + 1, mapMatrix, spreads):
                continue
            
            visitedMatrix[movedPos[0]][movedPos[1]] = 1
            newNode = (movedPos, depth + 1, visited + [movedPos])
            queue.append(newNode)

    return -1, -1


def checkSpreads(pos, depth, mapMatrix, spreads):
    spreadDirections = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for spread in spreads:
        spreadPos, directionIndex, spreadValue = (spread[0], spread[1]), spread[2], spread[3]
        spreadDirection = spreadDirections[directionIndex]

        if not ([spreadDirection] == getDirection(spreadPos, pos) or [] == getDirection(spreadPos, pos)):
            continue


        ##방향이 일치한 경우
        distance = getDistance(spreadPos, pos)

        if depth // spreadValue < distance:
            continue

        moved = 0
        flag = 0
        while moved < distance:
            moved +=1

            movedPos = (spreadPos[0] + moved * spreadDirection[0], spreadPos[1] + moved * spreadDirection[1])
            if mapMatrix[movedPos[0]][movedPos[1]] == 1:
                flag = 1
                break
        
        if flag == 1:
            continue

        return False
    
    return True


def getDirection(start, end):
    delta = (end[0] - start[0], end[1] - start[1])

    if delta[0] == 0 and delta[1] == 0:
        return []
    
    if delta[0] == 0:
        return [(0, int(delta[1] / abs(delta[1])))]
    
    if delta[1] == 0:
        return [(int((delta[0] / abs(delta[0]))), 0)]
    
    return [(int((delta[0] / abs(delta[0]))), 0), (0, int(delta[1] / abs(delta[1])))]

def getDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def checkIndexInMapMatrix(pos, N):
    if 0 <= pos[0] < N and 0 <= pos[1] < N:
        return True
    
    return False


def getExitInTimeWall(N, mapMatrix, M):
    for i in range(N):
        flag = 0
        for j in range(N):
            if mapMatrix[i][j] == 3:
                flag = 1
                timeWallStartPos = (i, j)
                break
        
        if flag == 1:
            break

    ##윗변, 아랫변 탐색
    for i in range(M):
        upperPos = (timeWallStartPos[0] - 1, timeWallStartPos[1] + i)
        downPos = (timeWallStartPos[0] + M, timeWallStartPos[1] + i)

        if mapMatrix[upperPos[0]][upperPos[1]] == 0:
            return upperPos, (0, M + i)
        
        if mapMatrix[downPos[0]][downPos[1]] == 0:
            return downPos, (3 * M - 1, M + i)
    
    ##좌변, 우변 탐색
    for i in range(M):
        leftPos = (timeWallStartPos[0] + i, timeWallStartPos[1] - 1)
        rightPos = (timeWallStartPos[0] + i, timeWallStartPos[1] + M)

        if mapMatrix[leftPos[0]][leftPos[1]] == 0:
            return leftPos, (M + i, 0)
        
        if mapMatrix[rightPos[0]][rightPos[1]] == 0:
            return rightPos, (M + i, 3 * M - 1)
        


def solution():
    N, M, F = map(int, input().split())

    mapMatrix = []
    for i in range(N):
        newRow = list(map(int, input().split()))
        mapMatrix.append(newRow)

        for j in range(N):
            if newRow[j] == 4:
                mapDest = (i, j)

    timeWallInfos = []
    for _ in range(5 * M):
        newTimeWallInfo = list(map(int, input().split()))
        timeWallInfos.append(newTimeWallInfo)

    spreadInfos = []
    for _ in range(F):
        newSpreadInfo = list(map(int, input().split()))
        spreadInfos.append(newSpreadInfo)

        



    timeWallMatrix, timeWallStartPoint = makeTimeWallMatrix(timeWallInfos, M)

    mapStartPoint, timeWallDest = getExitInTimeWall(N, mapMatrix, M)
    timeWallStartPoint = (timeWallStartPoint[0] + M, timeWallStartPoint[1] + M)

    turnInTimeWall = bfsInTimeWall(timeWallStartPoint, timeWallDest, timeWallMatrix, M)
    turnInTimeWall += 1
    result, visited = bfsIn2d(mapStartPoint, mapDest, mapMatrix, turnInTimeWall, spreadInfos)
    print(result)
solution()