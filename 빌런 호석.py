import sys
import copy
from collections import defaultdict

def solution():
    N, K, P, X = map(int, sys.stdin.readline().split())

    X = changeIntToList(X, K)
    N = changeIntToList(N, K)
    # print(X)
    # print(N)
    numDict = defaultdict(int)
    numDict[changeListToStr(X)] = 1
    answer = 0

    queue = [(X, P, 0)]

    while queue:
        node = queue.pop()
        numList, numRemainSwap, changeIndex = node[0], node[1], node[2]

        for i in range(10):
            numSwap = countNumSwap(numList[changeIndex], i)
            if numSwap > numRemainSwap:
                continue
            numListChanged = copy.deepcopy(numList)
            numListChanged[changeIndex] = i

            if changeIndex < K - 1:
                queue.append((numListChanged, numRemainSwap - numSwap, changeIndex + 1))

            if numDict[changeListToStr(numListChanged)] == 1:
                continue

            if not list1BiggerThenList2(numListChanged, N):
                if numListChanged == [0] * K:
                    continue
                # print(numListChanged)
                answer += 1
                numDict[changeListToStr(numListChanged)] = 1

    return answer



def makeDigitDict():
    digitDict = {}
    digitDict[0] = [1, 1, 1, 0, 1, 1, 1]
    digitDict[1] = [0, 0, 1, 0, 0, 0, 1]
    digitDict[2] = [0, 1, 1, 1, 1, 1, 0]
    digitDict[3] = [0, 1, 1, 1, 0, 1, 1]
    digitDict[4] = [1, 0, 1, 1, 0, 0, 1]
    digitDict[5] = [1, 1, 0, 1, 0, 1, 1]
    digitDict[6] = [1, 1, 0, 1, 1, 1, 1]
    digitDict[7] = [0, 1, 1, 0, 0, 0, 1]
    digitDict[8] = [1, 1, 1, 1, 1, 1, 1]
    digitDict[9] = [1, 1, 1, 1, 0, 1, 1]


    return digitDict

def countNumSwap(curNum, destNum):
    digitDict = makeDigitDict()

    curList = digitDict[curNum]
    destList = digitDict[destNum]
    numSwap = 0
    for i in range(len(curList)):
        if curList[i] != destList[i]:
            numSwap += 1

    return numSwap

def list1BiggerThenList2(list1, list2):
    return [list1, list2] != sorted([list1, list2])

def changeIntToList(num, listLength):
    strNum = str(num)
    returnList = []

    for i in range(len(strNum)):
        returnList.append(int(strNum[i]))

    if len(returnList) < listLength:
        returnList = [0] * (listLength - len(returnList)) + returnList

    return returnList


def changeListToStr(charList):
    returnInt = ""

    for i in range(len(charList)):
        returnInt += str(charList[i])

    return returnInt

print(solution())