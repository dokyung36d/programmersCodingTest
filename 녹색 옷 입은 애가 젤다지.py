import sys
import heapq

def solution(N):
    matrix = []
    for _ in range(N):
        newRow = list(map(int, sys.stdin.readline().split()))
        matrix.append(newRow)

    visitedMatrix = [[0 for _ in range(N)] for _ in range(N)]
    queue = [(matrix[0][0], (0, 0))] ##Cost, Pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    recordMatrix = [[10 ** 5 for _ in range(N)] for _ in range(N)]

    while queue:
        node = heapq.heappop(queue)
        cost, curPos = node[0], node[1]

        if curPos == (N - 1, N - 1):
            return cost

        visitedMatrix[curPos[0]][curPos[1]] = 1

        for direction in directions:
            movedPos = addTwoTuple(curPos, direction)

            if not checkIndex(movedPos, N):
                continue

            if visitedMatrix[movedPos[0]][movedPos[1]] == 1:
                continue

            if cost < recordMatrix[movedPos[0]][movedPos[1]]:
                recordMatrix[movedPos[0]][movedPos[1]] = cost
                heapq.heappush(queue, (cost + matrix[movedPos[0]][movedPos[1]], movedPos))


    return -1


def checkIndex(index, N):
    if 0 <= index[0] < N and 0 <= index[1] < N:
        return True
    
    return False

def addTwoTuple(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


if __name__ == "__main__":
    iteration = 0
    while True:
        iteration += 1
        N = int(sys.stdin.readline())
        if N == 0:
            break

        result = solution(N)
        print(f"Problem {iteration}: {result}")