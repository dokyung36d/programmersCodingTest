def makeTimeWallMatrix(infos, M):

    matrix = [[-1 for _ in range(3 * M)] for _ in range(3 * M)]

    ## East
    eastMatrix = []
    for i in range(0, M):
        eastMatrix.append(infos[i])
    matrix = applySmallMatrixToBigMatrix(matrix, eastMatrix, M ,2 * M, M)

    ## West
    westMatrix = []
    for i in range(M, 2 * M):
        westMatrix.append(infos[i])
    matrix = applySmallMatrixToBigMatrix(matrix, westMatrix, M, 0, M)

    ## South
    southMatrix = []
    for i in range(2 * M, 3 * M):
        southMatrix.append(infos[i])
    matrix = applySmallMatrixToBigMatrix(matrix, southMatrix, 2 * M, M, M)

    ## North
    northMatrix = []
    for i in range(3 * M, 4 * M):
        northMatrix.append(infos[i])
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


def moveInTimeWall(pos, direction, timeWallMatrix):
    
    movedPos = (pos[0] + direction[0], pos[1] + direction[1])

    if timeWallMatrix[movedPos[0]][movedPos[1]] != -1:
        return movedPos
    

    ## 2, 4 사분면에 존재하는 경우
    if checkDiagonalInTimeWallMatrix(movedPos):
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

    timeWallDest, mapStartPoint = getExitInTimeWall(N, mapMatrix, M)
    print(mapDest, timeWallStartPoint)
    print(timeWallDest, mapStartPoint)
# for row in timeWallMatrix:
#     print(row)
# print(moveInTimeWall((1, 5), (0, 1), timeWallMatrix))

solution()