# https://www.acmicpc.net/problem/20055

import sys
import heapq

def solution():
    N, K = map(int, sys.stdin.readline().split())
    beltList = list(map(int, sys.stdin.readline().split())) ##index : [0, 2 * N - 1]
    robotExist = [0] * len(beltList)

    startIndexPointer, endIndexPointer = 0, N - 1

    robotHeap = []
    numOuted = 0
    
    depth = 0
    while countZero(beltList) < K:
        depth += 1
        updatedRobotHeap = []

        ##Conveyer Belt Move
        startIndexPointer = (startIndexPointer - 1) % (2 * N)
        endIndexPointer = (endIndexPointer - 1) % (2 * N)

        while robotHeap:
            prevDepth, robotPos = heapq.heappop(robotHeap)
            if robotPos == endIndexPointer:
                robotExist[robotPos] -= 1
                continue

            movedRobotPos = (robotPos + 1) % (2 * N) ##Robot Move
            if robotExist[movedRobotPos] != 0 or beltList[movedRobotPos] == 0: ##Can not move
                heapq.heappush(updatedRobotHeap, (prevDepth, robotPos))
                continue

            beltList[movedRobotPos] -= 1
            robotExist[robotPos] -= 1

            if movedRobotPos == endIndexPointer:
                continue

            heapq.heappush(updatedRobotHeap, (prevDepth, movedRobotPos))
            robotExist[movedRobotPos] += 1

        

        if beltList[startIndexPointer] != 0:
            heapq.heappush(updatedRobotHeap, (depth, startIndexPointer))
            robotExist[startIndexPointer] += 1
            beltList[startIndexPointer] -= 1

            
        robotHeap = updatedRobotHeap

    
    return depth

def countZero(list1):
    num = 0
    for i in range(len(list1)):
        if list1[i] == 0:
            num += 1
    
    return num

print(solution())