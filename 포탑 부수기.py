import heapq

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

            heapq.heappush(cannonAttackHeap, (value, 0, -(i + j), -j))
            heapq.heappush(cannonDefenseHeap, (-value, 0, i + j,  j))

    print(lazerAttack((0, 1), (2, 3), N, M, mapMatrix))



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
                return visited[:] + [defenserPos]

            visitedMatrix[movedPos[0]][movedPos[1]] = 1
            queue.append((movedPos, visited + [movedPos]))

    return []

    

def bombAttack(defenserPos):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    

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