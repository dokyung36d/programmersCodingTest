import sys
import bisect
import heapq
from collections import defaultdict

def solution():
    N, C = map(int, sys.stdin.readline().split())
    spotList = []
    for _ in range(N):
        spotList.append(int(sys.stdin.readline()))
    spotList = sorted(spotList)
    
    headGap = 1
    tailGap = spotList[-1] - spotList[0]
    maxGap = headGap
    while headGap <= tailGap:
        midGap = (headGap + tailGap) // 2
        numHouse = getHouseNumWhenGapIsGiven(spotList, midGap)
        
        if numHouse >= C:
            headGap = midGap + 1
            maxGap = max(maxGap, midGap)
        else:
            tailGap = midGap - 1

    
    return maxGap


def getHouseNumWhenGapIsGiven(spotList, gap):
    numHouse = 1
    prevHouse = spotList[0]

    for i in range(1, len(spotList)):
        newHouse = spotList[i]
        if newHouse - prevHouse >= gap:
            numHouse += 1
            prevHouse = newHouse

    return numHouse

print(solution())