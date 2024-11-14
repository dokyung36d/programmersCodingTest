##https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
import copy
import bisect
from collections import defaultdict
from os import remove


def queen(indices):
    global n
    removedIndices = []

    row, col = indices[0], indices[1]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    removedIndices.append(indices)

    for direction in directions:
        mutiply = 1
        rowDirection, colDirection = direction[0], direction[1]

        while True:
            rowChanged = row + mutiply * rowDirection
            colChanged = col + mutiply * colDirection

            if not checkIndex((rowChanged, colChanged)):
                break

            index = bisect.bisect_left(removedIndices, (rowChanged, colChanged))
            removedIndices.insert(index, (rowChanged, colChanged))

            mutiply += 1

    return removedIndices


##Just For Visualization
def applyToMap(mapInfo, removedIndices):
    global matrix

    for removedIndex in removedIndices:
        matrix[removedIndex[0]][removedIndex[1]] = 1

def applyToDict(mapDict, removedIndices):
    mapDict = copy.deepcopy(mapDict)
    for removedIndex in removedIndices:
        mapDict[removedIndex] = 1

    return mapDict

def applyToSortedList(sortedList, removedIndices):
    sortedList = sortedList[:]

    if len(sortedList) == 0:
        sortedList.append(removedIndices[0])

    for removedIndex in removedIndices:
        index = bisect.bisect_left(sortedList, removedIndex)

        if sortedList[index] == removedIndex:
            continue

        sortedList.insert(index, removedIndex)

    return sortedList



def setQueen(startIndices, numRemainQueen, queenIndices):
    global n, matrix, cnt

    for i in range(startIndices[0], n):
        for j in range(startIndices[1], n):
            # removedIndices = queen((i, j))


            ## if already chose
            if not checkCompatibleWithAnotherQueenByIndex((i, j), queenIndices):
                continue

            if numRemainQueen == 1:
                cnt += 1
                continue

            nextIndices = getNextIndex((i, j))
            if nextIndices == False:
                return


            setQueen(nextIndices, numRemainQueen - 1, queenIndices + [(i, j)])


def checkIndex(indices):
    if indices[0] < 0 or indices[0] >= n or indices[1] < 0 or indices[1] >= n:
        return False

    return True

def getNextIndex(indices):
    global n
    row, col = indices[0], indices[1]

    if row == n - 1 and col == n - 1:
        return False

    return (row + 1, 0)

    # if col == n - 1:
    #     return (row + 1, 0)
    #
    # return (row, col + 1)

def checkCompatibleWithAnotherQueen(removedIndices, queenIndices):
    for queenIndex in queenIndices:
        index = bisect.bisect_left(removedIndices, queenIndex)

        if removedIndices[index] == queenIndex:
            return False

    return True

def checkCompatibleWithAnotherQueenByIndex(curIndex, queenIndices):
    for queenIndex in queenIndices:
        rowDelta, colDelta = queenIndex[0] - curIndex[0], queenIndex[1] - curIndex[1]

        if rowDelta == 0 or colDelta == 0:
            return False

        if abs(rowDelta) == abs(colDelta):
            return False

    return True

# cnt = 0
# n = int(input())
# setQueen((0, 0), n, [])
# print(cnt)

T = int(input())

for _ in range(1, T + 1):
    n = int(input())
    cnt = 0
    setQueen((0, 0), n, [])

    print(f"#{_} {cnt}")

# removedIndices = queen((2, 1))
#
# for removedIndex in removedIndices:
#     matrix[removedIndex[0]][removedIndex[1]] = 1
#
# for row in matrix:
#     print(row)