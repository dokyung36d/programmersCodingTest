import bisect


def solution(numDump, mapInfo):
    sortedMapInfo = [mapInfo[0]]
    for i in range(1, len(mapInfo)):
        insertIndex = bisect.bisect_left(sortedMapInfo, mapInfo[i])
        sortedMapInfo.insert(insertIndex, mapInfo[i])


    for _ in range(numDump):
        minNum = sortedMapInfo.pop(0)
        maxNum = sortedMapInfo.pop(-1)

        minNum += 1
        maxNum -= 1

        minNumIndex = bisect.bisect_left(sortedMapInfo, minNum)
        sortedMapInfo.insert(minNumIndex, minNum)

        maxNumIndex = bisect.bisect_left(sortedMapInfo, maxNum)
        sortedMapInfo.insert(maxNumIndex, maxNum)

    return sortedMapInfo[-1] - sortedMapInfo[0]

for _ in range(10):
    numDump = int(input())
    info = list(map(int, input().split()))

    result = solution(numDump, info)
    print(f"#{_ + 1} {result}")
