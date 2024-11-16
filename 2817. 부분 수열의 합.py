from collections import defaultdict

def solution(numList, k):
    dpDict = defaultdict(int)
    dpDict[0] = 1

    numList.sort()


    for i in range(len(numList)):
        num = numList[i]

        keyList = list(dpDict.keys())
        keyList.sort(reverse = True)

        for key in list(keyList):
            plusNum = key + num

            if plusNum > k:
                continue
            dpDict[key + num] += dpDict[key]

    return dpDict[k]


T = int(input())

for _ in range(1, T + 1):
    n, k = map(int, input().split())

    numList = list(map(int, input().split()))
    result = solution(numList, k)

    print(f"#{_} {result}")