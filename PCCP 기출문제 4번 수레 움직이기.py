def solution(maze):
    redPos, bluePos = getRedBluePos(maze)
    answer = bfs(redPos, bluePos, maze)
    return answer

directions = {0 : (-1, 0), 1 : (1, 0), 2 : (0, -1), 3 : (0, 1)}

def checkIndex(pos, n, m):
    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= m:
        return False
    
    return True

def checkMoveAvailable(pos, visited, mapInfo):
    if not checkIndex(pos, len(mapInfo), len(mapInfo[0])):
        return False
    
    if mapInfo[pos[0]][pos[1]] == 5:
        return False

    if pos in visited:
        return False
    
    return True
    
    # if pos == opposPos:
    #     return False

def bfs(redPos, bluePos, mapInfo):
    num = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(redPos, bluePos, [redPos], [bluePos], 0)]
    
    while queue:
        num += 1
        node = queue.pop(0)
        redPos, bluePos, redVisited, blueVisited, depth = node[0], node[1], node[2], node[3], node[4]
        
        redFlag = 0
        blueFlag = 0
        
        redMoveCandidate = []
        blueMoveCandidate = []
        
        if mapInfo[redPos[0]][redPos[1]] == 3:
            redFlag = 1
            redMoveCandidate.append(redPos)
        if mapInfo[bluePos[0]][bluePos[1]] == 4:
            blueFlag = 1
            blueMoveCandidate.append(bluePos)
            
            
        if redFlag == 0:
            for direction in directions:
                redMovedPos = addTwoTuple(redPos, direction)
                if not checkMoveAvailable(redMovedPos, redVisited, mapInfo):
                    continue
                redMoveCandidate.append(redMovedPos)
        
        if blueFlag == 0:
            for direction in directions:
                blueMovedPos = addTwoTuple(bluePos, direction)
                if not checkMoveAvailable(blueMovedPos, blueVisited, mapInfo):
                    continue
                
                blueMoveCandidate.append(blueMovedPos)
        
        if len(redMoveCandidate) == 0 or len(blueMoveCandidate) == 0:
            continue
                                         
                
        for i in range(len(redMoveCandidate)):
            for j in range(len(blueMoveCandidate)):
                redMovedPos, blueMovedPos = redMoveCandidate[i], blueMoveCandidate[j]
                if redMovedPos == blueMovedPos:
                    continue
                    
                if redMovedPos == bluePos and blueMovedPos == redPos:
                    continue
                    
                if mapInfo[redMovedPos[0]][redMovedPos[1]] == 3 and mapInfo[blueMovedPos[0]][blueMovedPos[1]] == 4:
                    return depth + 1
                    
                newNode = (redMovedPos, blueMovedPos, redVisited + [redMovedPos], blueVisited + [blueMovedPos], depth + 1)
                queue.append(newNode)
    return 0

def getRedBluePos(mapInfo):
    for i in range(len(mapInfo)):
        for j in range(len(mapInfo[0])):
            if mapInfo[i][j] == 1:
                redPos = (i, j)
            if mapInfo[i][j] == 2:
                bluePos = (i, j)
                
    return redPos, bluePos
            
        
def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])