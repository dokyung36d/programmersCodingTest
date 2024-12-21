## https://www.acmicpc.net/problem/14719

import sys
import heapq
import bisect

def solution():
    H, W = map(int, sys.stdin.readline().split())
    blockList = list(map(int, sys.stdin.readline().split()))

    blockQueue = []

    for i in range(len(blockList)):
        heapq.heappush(blockQueue, (-blockList[i], i))

    maxBlock, maxBlockIndex = heapq.heappop(blockQueue)

    columnList = [maxBlockIndex]

    while blockQueue:
        node = heapq.heappop(blockQueue)
        blockHeight, blockIndex = -node[0], node[1]
        if blockHeight == 0:
            continue
        insertIndex = bisect.bisect_left(columnList, blockIndex)

        if insertIndex == 0 or insertIndex == len(columnList):
            columnList.insert(insertIndex, blockIndex)

    
    answer = 0

    for i in range(0, len(columnList) - 1):
        startIndex, endIndex = columnList[i], columnList[i + 1]
        
        rainDropHeight = min([blockList[startIndex], blockList[endIndex], H])
        for j in range(startIndex + 1, endIndex):
            numRainDrop = max(0, rainDropHeight - blockList[j])
            answer += numRainDrop

    return answer




print(solution())