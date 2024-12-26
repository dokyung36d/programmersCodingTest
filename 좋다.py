import sys
import bisect
from collections import defaultdict

def solution():
    N = int(sys.stdin.readline())
    if N == 1 or N == 2:
        return 0

    
    numList = list(map(int, sys.stdin.readline().split()))
    numList = sorted(numList)

    totalAppearDict = defaultdict(int)
    answerDict = defaultdict(int)

    for i in range(len(numList)):
        totalAppearDict[numList[i]] += 1

    answer = 0
    for i in range(len(numList)):
        firstIterationFlag = 0
        for j in range(len(numList)):
            if i == j:
                continue
            appearDict = defaultdict(int)

            sumValue = numList[i]
            firstNum = numList[j]
            secondNum = sumValue - firstNum

            appearDict[sumValue] += 1
            appearDict[firstNum] += 1
            appearDict[secondNum] += 1

            secondIterationFlag = 0
            for key in appearDict.keys():
                if appearDict[key] > totalAppearDict[key]:
                    secondIterationFlag = 1
                    break

            if secondIterationFlag == 0:
                firstIterationFlag = 1
                break

        if firstIterationFlag == 1:
            answer += 1
            

    return answer


print(solution())