import heapq
from collections import defaultdict

def solution():
    N, M, K = map(int, input().split())

    cannonAttackHeap = []
    cannonDefenseHeap = []
    mapMatrix = []
    for i in range(N):
        newRow = list(map(int, input().split()))
        mapMatrix.append(newRow)

        for j in range(M):
            value = newRow[j]
            if value == 0:
                continue
            attackNode, defenseNode = makeAttackDefenseHeapNode((i, j), 0, value)

            heapq.heappush(cannonAttackHeap, attackNode)
            heapq.heappush(cannonDefenseHeap, defenseNode)


    for i in range(1, K + 1):
        attacker = heapq.heappop(cannonAttackHeap)
        attackerPos = attacker[-1]
        mapMatrix[attackerPos[0]][attackerPos[1]] += (N + M)
        power = mapMatrix[attackerPos[0]][attackerPos[1]]

        defenser = heapq.heappop(cannonDefenseHeap)
        defenserPos = defenser[-1]

        sidePoses, sidePosDict = lazerAttack(attackerPos, defenserPos, N, M, mapMatrix)
        if sidePoses == []:
            sidePoses, sidePosDict = bombAttack(defenserPos, N, M, mapMatrix)


        mapMatrix = applyEffectToMapMatrix(defenserPos, sidePoses, power, mapMatrix)


        cannonAttackHeap, cannonDefenseHeap, mapMatrix = prepareCannon(cannonAttackHeap, cannonDefenseHeap, attackerPos, defenserPos, mapMatrix, i, sidePosDict)

        for row in mapMatrix:
            print(row)
        print()
    node = heapq.heappop(cannonDefenseHeap)
    print(-node[0])

    # print(lazerAttack((0, 1), (2, 3), N, M, mapMatrix))
    # print(bombAttack((2, 3), N, M, mapMatrix))



def lazerAttack(attackerPos, defenserPos, N, M, mapMatrix):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(attackerPos, [])]

    visitedMatrix = [[0 for _ in range(M)] for _ in range(N)]
    visitedMatrix[attackerPos[0]][attackerPos[1]] = 1

    while queue:
        node = queue.pop(0)
        currentPos, visited = node[0], node[1]
        
        for direction in directions:
            movedPos = move(currentPos, direction, N, M)

            if not checkMoveAvailable(movedPos, mapMatrix):
                continue

            if visitedMatrix[movedPos[0]][movedPos[1]] == 1:
                continue


            if movedPos == defenserPos:
                sidePosDict = makeSidePosDict(visited)
                return visited, sidePosDict

            visitedMatrix[movedPos[0]][movedPos[1]] = 1
            queue.append((movedPos, visited + [movedPos]))

    return [], defaultdict(int)

    

def bombAttack(defenserPos, N, M, mapMatrix):
    sidePoses = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    sidePosDict = defaultdict(int)

    for direction in directions:
        movedPos = move(defenserPos, direction, N, M)

        if not checkMoveAvailable(movedPos, mapMatrix):
            continue
        sidePoses.append(movedPos)
        sidePosDict[movedPos] = 1
    

    return sidePoses, sidePosDict

def makeSidePosDict(sidePoses):
    posDict = defaultdict(int)

    for sidePos in sidePoses:
        posDict[sidePos] = 1

    return posDict

def applyEffectToMapMatrix(defederPos, sidePoses, power, mapMatrix):
    sidePower = power // 2
    
    mapMatrix[defederPos[0]][defederPos[1]] -= min(power, mapMatrix[defederPos[0]][defederPos[1]])

    for sidePos in sidePoses:
        mapMatrix[sidePos[0]][sidePos[1]] -= min(sidePower, mapMatrix[sidePos[0]][sidePos[1]])


    return mapMatrix


def prepareCannon(attackHeap, defenseHeap, attackedPos, defensedPos, mapMatrix, turn, sidePosDict):
    newAttackHeap = []
    newDefenseHeap = []

    while attackHeap:
        node = heapq.heappop(attackHeap)
        pos = node[-1]
        prevAttack = node[1]

        if mapMatrix[pos[0]][pos[1]] == 0:
            continue

        if sidePosDict[pos] == 1:
            continue

        if pos != defensedPos:
            mapMatrix[pos[0]][pos[1]] += 1

        newAttackNode, newDefenseNode = makeAttackDefenseHeapNode(pos, prevAttack, mapMatrix[pos[0]][pos[1]])
        heapq.heappush(newAttackHeap, newAttackNode)
        heapq.heappush(newDefenseHeap, newDefenseNode)

    newAttackNode, newDefenseNode = makeAttackDefenseHeapNode(attackedPos, turn, mapMatrix[attackedPos[0]][attackedPos[1]])
    heapq.heappush(newAttackHeap, newAttackNode)
    heapq.heappush(newDefenseHeap, newDefenseNode)


    return newAttackHeap, newDefenseHeap, mapMatrix


def makeAttackDefenseHeapNode(pos, prevAttack, value):
    attackNode = (value, -prevAttack, -(pos[0] + pos[1]), -pos[1], pos)
    defenseNode = (-value, prevAttack, pos[0] + pos[1], pos[1], pos)

    return attackNode, defenseNode

def move(pos, direction, N, M):
    movedPos = addTwoTuple(pos, direction)
    movedPos = (movedPos[0] % N, movedPos[1] % M)

    return movedPos

def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def checkMoveAvailable(pos, mapMatrix):
    if mapMatrix[pos[0]][pos[1]] == 0:
        return False
    
    return True

solution()