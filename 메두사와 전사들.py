##SWEA 체스 문제랑 유사하게 풀기

import bisect
from collections import defaultdict

N, M = map(int, input().split())

def calculateDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def getMainDirections(pos, startPos):
    deltaRow, deltaCol = pos[0] - startPos[0], pos[1] - startPos[1]

    if deltaRow == 0:
        return [(0, int(deltaCol / abs(deltaCol)))]
    
    if deltaCol == 0:
        return [(int(deltaRow / abs(deltaRow)), 0)]
    
    if abs(deltaRow) == abs(deltaCol):
        return [(int(deltaRow / abs(deltaRow)), 0), (0, int(deltaCol / abs(deltaCol)))]
    
    if abs(deltaRow) > abs(deltaCol):
        return [(int(deltaRow / abs(deltaRow)), 0)]
    
    if abs(deltaRow) < abs(deltaCol):
        return [(0, int(deltaCol / abs(deltaCol)))]
    

def getWarrirorDirection(pos, medusaPos, warriorRocekdPos, medusaDirection):
    rowDelta, colDelta = warriorRocekdPos[0] - medusaPos[0], warriorRocekdPos[1] - medusaPos[1]
    pass

def subtractDirectionFromDelta(delta, direction):
    pass
    
def medusaMove():
    global medusaPos, parkCol
    bestPos = medusaPos
    bestDistance = calculateDistance(medusaPos, parkPos)

    directionDict = {0 : (-1, 0), 1 : (1, 0), 2 : (0, -1), 3 : (0, 1)}

    for i in range(4):
        direction = directionDict[i]

        movedPos = (medusaPos[0] + direction[0], medusaPos[1] + direction[1])
        movedDistance = calculateDistance(movedPos, parkPos)

        if movedDistance < bestDistance:
            bestDistance = movedDistance
            bestPos = movedPos

    return bestPos

def medusa():
    global medusaPos, soldierList

    ##상하좌우 순서대로, 경계에 있는 값들이 상황에 따라 masking되는 곳이 달라짐.
    directionDict = {0 : (-1, 0), 1 : (1, 0), 2 : (0, -1), 3 : (0, 1)}


    for i in range(4):
        direction = directionDict[i]

        


medusaRow, medusaCol, parkRow, parkCol = map(int, input().split())
medusaPos = (medusaRow, medusaCol)
parkPos = (parkRow, parkCol)

soldierList = []
soldierPosList = list(map(int, input().split()))
soldierList.append((calculateDistance((medusaRow, medusaCol), (soldierPosList[0], soldierPosList[1])),
                    (soldierPosList[0], soldierPosList[1])))

for i in range(2, 2 * M, 2):
    soldierPos = (soldierPosList[i], soldierPosList[i + 1])
    distance = calculateDistance((medusaRow, medusaCol), soldierPos)

    index = bisect.bisect_left(soldierList, (distance, soldierPos))
    soldierList.insert(index, (distance, soldierPos))

mapInfo = []
for _ in range(N):
    newRow = list(map(int, input().split()))
    mapInfo.append(newRow)
print(soldierList)