import sys
from collections import defaultdict
import heapq

def solution():
    N, M = map(int, sys.stdin.readline().split())

    ladderDict = defaultdict(int)
    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        ladderDict[start] = end

    snakeDict = defaultdict(int)
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        snakeDict[start] = end

    visitedDict = defaultdict(int)
    visitedDict[1] = 1
    queue = [(0, -1)] ##depth, -currentNum

    while queue:
        node = heapq.heappop(queue)
        depth, currentNum = node[0], -node[1]

        for i in range(1, 7):
            movedNum = currentNum + i
            dest = getDest(movedNum, ladderDict, snakeDict)
            if visitedDict[dest] != 0:
                continue

            if dest == 100:
                return depth + 1

            heapq.heappush(queue, (depth + 1, -dest))
            visitedDict[dest] = 1





def getMinimumRollDice(currentNum, dpList, ladderDict, snakeDict):
    currentNumIndex = currentNum - 1
    minNumRollDice = 10 ** 10
    for i in range(1, 7):
        prevNum = max(1, currentNum - i)
        prevNumIndex = prevNum - 1
        if dpList[prevNumIndex] + 1 < minNumRollDice:
            minNumRollDice = dpList[prevNumIndex] + 1


    # if ladderDict[currentNum] != 0:
    #     dest = ladderDict[currentNum]
    #     destIndex = dest - 1
    #     dpList[destIndex] = minNumRollDice
    #     return dpList
    
    # if snakeDict[currentNumIndex] != 0:
    #     return dpList
    # dpList[currentNumIndex] = minNumRollDice

    dest = getDest(currentNum, ladderDict, snakeDict)
    destIndex = dest - 1

    dpList[destIndex] = min(minNumRollDice, dpList[destIndex])
 
    return dpList

def getDest(currentNum, ladderDict, snakeDict):
    while ladderDict[currentNum] != 0 or snakeDict[currentNum] != 0:
        if ladderDict[currentNum] != 0:
            currentNum = ladderDict[currentNum]
            
        elif snakeDict[currentNum] != 0:
            currentNum = snakeDict[currentNum]

    return currentNum 

print(solution())