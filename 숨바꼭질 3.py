## https://www.acmicpc.net/problem/13549

from collections import defaultdict
import sys
import heapq

def solution():
    N, K = map(int, sys.stdin.readline().split())
    if N >= K:
        return N - K
    queue = []
    heapq.heappush(queue, (0, N))
    visitedDict = defaultdict(int)

    visitedDict[N] = 1

    while queue:
        depth, value = heapq.heappop(queue)
        # print(depth, value)
        
        visitedDict[value] = 1

        if value == K:
            return depth


        if visitedDict[value - 1] == 0 and value >= 1:
            heapq.heappush(queue, (depth + 1, value - 1))

        if visitedDict[value + 1] == 0:
            heapq.heappush(queue, (depth + 1, value + 1))
            

        while value <= K and value != 0:
            # print(value)
            if visitedDict[2 * value] == 0:
                visitedDict[2 * value] = visitedDict[value]
                heapq.heappush(queue, (depth, 2 * value))

            value = 2 * value


print(solution())