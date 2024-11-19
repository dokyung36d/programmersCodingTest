##SWEA 체스 문제랑 유사하게 풀기

import bisect
from collections import defaultdict

N, M = map(int, input().split())

def calculateDistance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def checkIndex(pos):
    if pos[0] < 0 or pos[0] > N or pos[1] < 0 or pos[1] > N:
        return False
    
    return True

def getDirections(pos, startPos):
    deltaRow, deltaCol = pos[0] - startPos[0], pos[1] - startPos[1]

    if deltaRow == 0:
        return [(0, int(deltaCol / abs(deltaCol)))]
    
    if deltaCol == 0:
        return [(int(deltaRow / abs(deltaRow)), 0)]
    
    if abs(deltaRow) == abs(deltaCol):
        return [(int(deltaRow / abs(deltaRow)), int(deltaCol / abs(deltaCol)))]
        # return [(int(deltaRow / abs(deltaRow)), 0), (0, int(deltaCol / abs(deltaCol)),
        #                                               (int(deltaRow / abs(deltaRow)), int(deltaCol / abs(deltaCol))))]
    
    if abs(deltaRow) > abs(deltaCol):
        return [(int(deltaRow / abs(deltaRow), 0)), (int(deltaRow / abs(deltaRow), int(deltaCol / abs(deltaCol))))]
    
    if abs(deltaRow) < abs(deltaCol):
        return [(0, int(deltaCol / abs(deltaCol))), (int(deltaRow / abs(deltaRow), int(deltaCol / abs(deltaCol))))]
    
    # if abs(deltaRow) > abs(deltaCol):
    #     return [(int(deltaRow / abs(deltaRow)), 0)]
    
    # if abs(deltaRow) < abs(deltaCol):
    #     return [(0, int(deltaCol / abs(deltaCol)))]
    


def getSideDirections(mainDirection):
    if mainDirection[0] == 0:
        return [(-1, mainDirection[1]), (1, mainDirection[1])]
    
    if mainDirection[1] == 0:
        return [(mainDirection[0], -1), (mainDirection[0], 1)]
    
def moveMedusa():
    global medusaPos, parkCol
    bestPos = medusaPos
    bestDistance = calculateDistance(medusaPos, parkPos)

    directionDict = {0 : (-1, 0), 1 : (1, 0), 2 : (0, -1), 3 : (0, 1)}

    for i in range(4):
        direction = directionDict[i]

        movedPos = (medusaPos[0] + direction[0], medusaPos[1] + direction[1])

        if not checkIndex(movedPos):
            continue

        movedDistance = calculateDistance(movedPos, parkPos)

        if movedDistance < bestDistance:
            bestDistance = movedDistance
            bestPos = movedPos

    return bestPos

def medusa():
    global medusaPos, soldierList

    ##상하좌우 순서대로, 경계에 있는 값들이 상황에 따라 masking되는 곳이 달라짐.
    directionDict = {0 : (-1, 0), 1 : (1, 0), 2 : (0, -1), 3 : (0, 1)}
    maxNumRockedSoldier = 0


    for i in range(4):
        directions = []
        directions.append(directionDict[i])
        directions.extend(getSideDirections(directionDict[i]))

        numRockerSoldier, rockedSoldierList = medusaWatch(directions)
        if numRockerSoldier > maxNumRockedSoldier:
            maxNumRockedSoldier = numRockerSoldier
            maxNumMedusaDirection = directions
            maxRockedSoldierList = rockedSoldierList

    assert maxNumMedusaDirection is not None

    return maxNumMedusaDirection, maxRockedSoldierList


def medusaWatch(medusaDirections, medusaMainDirection):
    global medusaPos

    num = 0
    rockedSoldierList = []

    for soldier in soldierList:
        soldierPos = soldier[1]
        
        if checkAvailablePos(soldierPos, medusaDirections, rockedSoldierList):
            continue

        directions = getDirections(soldierPos, medusaPos)
        if medusaMainDirection not in directions:
            directions.append(medusaMainDirection)

    
        num += 1
        rockedSoldierList.append((soldierPos, directions))

    return num, rockedSoldierList
    
def blindByRockedSoldier(pos, rockedSoldierList):
    for rockedSoldier in rockedSoldierList:
        rockedSoldierPos = rockedSoldier[0]
        directions = getDirections(pos, rockedSoldierPos)

        ## At least one gets blind, then survive
        for direction in directions:
            if direction in rockedSoldier[1]:
                return True
            
    return False

def checkBelong(pos, originPos, originDirections):
    directions = getDirections(pos, originPos)

    for direction in directions:
        if direction not in originDirections:
            return False
        
    return True

def checkAvailablePos(pos, medusaDirection, rockedSoldierList):
    global medusaPos

    if not checkBelong(pos, medusaPos, medusaDirection):
        return True
    
    for rockedSoldier in rockedSoldierList:
        if checkBelong(pos, rockedSoldier[0], rockedSoldier[1]):
            return True
        
    return False



def soldierMove(rockedSoldierList, medusaDirections, directionDict, numMoved, numAttacked):
    global soldierList, medusaPos

    ##can error happen
    ##At Least one Soldier is captured
    movedSoldierList = []
    movedSoldierList.append((calculateDistance(rockedSoldierList[0][0], medusaPos), rockedSoldierList[0][0]))

    for i in range(1, len(movedSoldierList)):
        value = (calculateDistance(rockedSoldierList[i][0], medusaPos), rockedSoldierList[i][0])
        index = bisect.bisect_left(movedSoldierList, value)
        movedSoldierList.insert(index, value)


    for soldier in soldierList:
        if soldier in rockedSoldierList:
            continue

        distance = calculateDistance(soldier, medusaPos)
        moveFlag = 0
        attackFlag = 0

        for i in range(4):
            direction = directionDict[i]
            movedPos = addTwoTuple(soldier, direction)

            if not checkIndex(movedPos):
                continue

            if not checkAvailablePos(movedPos, medusaPos, medusaDirections):
                continue

            movedDistance = calculateDistance(movedPos, medusaPos)
            if movedDistance < distance:
                moveFlag = 1
                distance = movedDistance
                soldier = movedPos

            if movedDistance == 0:
                attackFlag = 1
                numAttacked += 1
                break

        if moveFlag == 1:
            numMoved += 1

        if attackFlag == 1:
            continue

        index = bisect.bisect_left(movedSoldierList, (distance, movedPos))
        movedSoldierList.insert(index, (distance, movedPos))

    soldierList = movedSoldierList

    
    return numMoved, numAttacked


def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

        


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

firstMoveDirection = {0 : (-1, 0), 1 : (1, 0), 2 : (0, -1), 3 : (0, 1)}
secondMoveDirection = {0 : (0, -1), 1 : (0, 1), 2 : (-1, 0), 3 : (1, 0)}

while True:
    movedMedusaPos = moveMedusa()

    if movedMedusaPos == medusaPos:
        print(-1)
        break

    medusaPos = movedMedusaPos

    maxDirection, rockedSoldierList = medusa()

    numMoved = 0
    numAttacked = 0

    numMoved, numAttacked = soldierMove(rockedSoldierList, maxDirection, firstMoveDirection, numMoved, numAttacked)
    numMoved, numAttacked = soldierMove(rockedSoldierList, maxDirection, secondMoveDirection, numMoved, numAttacked)
