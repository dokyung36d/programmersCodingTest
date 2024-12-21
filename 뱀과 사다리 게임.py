import sys
from collections import defaultdict

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

    dpList = [10 ** 10] * 100 ##[0, 100)
    dpList[0] = 0
    for i in range(1, 100):
        dpList = getMinimumRollDice(i + 1, dpList, ladderDict, snakeDict)

    return dpList[-1]


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
    if dest == currentNum:
        dpList[currentNumIndex] = min(minNumRollDice, dpList[currentNumIndex])

    elif dest > currentNum:
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