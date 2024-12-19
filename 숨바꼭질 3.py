## https://www.acmicpc.net/problem/13549

from collections import defaultdict
import sys
import heapq

def solution():
    N, K = map(int, sys.stdin.readline().split())
    queue = []
    heapq.heappush(queue, (0, N))
    dpDict = defaultdict(int)

    dpDict[N] = 1

    while queue:
        depth, value = heapq.heappop(queue)
        # print(depth, value)
        
        if value == K:
            return depth

        assert dpDict[value] != 0


        if dpDict[value - 1] == 0 and value >= 1:
            dpDict[value - 1] = dpDict[value] + 1
            heapq.heappush(queue, (depth + 1, value - 1))

        if dpDict[value + 1] == 0:
            dpDict[value + 1] = dpDict[value] + 1
            heapq.heappush(queue, (depth + 1, value + 1))

        while value <= K and value != 0:
            # print(value)
            if dpDict[2 * value] == 0:
                dpDict[2 * value] = dpDict[value]
                heapq.heappush(queue, (depth, 2 * value))
            
            value = 2 * value


print(solution())