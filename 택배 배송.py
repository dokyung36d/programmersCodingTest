from collections import defaultdict
import sys
import heapq

def solution():
    N, M = map(int, sys.stdin.readline().split())

    edgeDict = defaultdict(list)
    determined = [0] * N
    determined[0] = 1
    shortestCostList = [0] * N

    for _ in range(M):
        A_i, B_i, C_i = map(int, sys.stdin.readline().split())
        A_i -= 1
        B_i -= 1

        edgeDict[A_i].append((B_i, C_i))
        edgeDict[B_i].append((A_i, C_i))

    queue = []
    for i in range(len(edgeDict[0])):
        dest, numCow = edgeDict[0][i]
        heapq.heappush(queue, (numCow, dest))


    while queue:
        node = heapq.heappop(queue)
        cost, currentPos = node[0], node[1]

        if determined[currentPos] == 1:
            continue
        
        shortestCostList[currentPos] = cost
        determined[currentPos] = 1
        
        for i in range(len(edgeDict[currentPos])):
            dest, numCow = edgeDict[currentPos][i]
            updatedCost = cost + numCow

            if determined[dest] == 1:
                continue

            heapq.heappush(queue, (updatedCost, dest))

    
    return shortestCostList[-1]

        


print(solution())