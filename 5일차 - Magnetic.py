import bisect
from collections import defaultdict

def solution(matrix):
    answer = 0
    for i in range(len(matrix)):
        row = getRow(matrix, i)
        result = processCol(row)
        answer += result


    return answer

def getRow(matrix, col):
    returnList = []
    for i in range(len(matrix)):
        returnList.append(matrix[i][col])

    return returnList

def processCol(col):
    sList = []
    for i in range(len(col)):
        if col[i] == 2:
            sList.append(i)

    intersectDict = defaultdict(int)

    for i in range(len(col)):
        if col[i] == 0 or col[i] == 2:
            continue

        index = bisect.bisect_left(sList, i)

        if index >= len(sList):
            continue

        intersectDict[index] = 1

    return len(intersectDict.keys())



T = 10

for _ in range(1, T + 1):
    matrix = []
    n = int(input())
    for i in range(n):
        newRow = list(map(int, input().split()))
        matrix.append(newRow)


    result = solution(matrix)

    print(f"#{_} {result}")