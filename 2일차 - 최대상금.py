import copy


def solution(numList, switchNum, answer = ""):
    global duplicates

    maxNum = int(switchListToStr(numList))
    if switchNum == 0:
        answer += switchListToStr(numList)
        return answer

    if len(numList) == 2:
        if duplicates and switchNum >= 3:
            answer += str(numList[0])
            answer += str(numList[1])

        elif switchNum % 2 == 0:
            answer += str(numList[0])
            answer += str(numList[1])

        else:
            answer += str(numList[1])
            answer += str(numList[0])

        return answer

    maxNumInNumList = max(numList)
    # maxNumIndex = len(numList) - numList[::-1].index(maxNum) - 1
    maxNumIndices = []
    for i in range(len(numList) - 1, -1, -1):
        if numList[i] == maxNumInNumList:
            maxNumIndices.append(i)

    index = 0
    while index != maxNumIndices[0]:
        if numList[index] != maxNumInNumList:
            break

        index += 1

    ## maxNum 앞의 값들이 전부 maxNum인 경우
    if index == maxNumIndices[0]:
        return solution(numList[1:], switchNum, answer + str(numList[0]))


    for i in range(len(maxNumIndices)):
        switchedNumList = switchIndex(numList, index, maxNumIndices[i])
        result = int(solution(switchedNumList[1:], switchNum - 1, answer + str(switchedNumList[0])))

        if result > maxNum:
            maxNum = result

    return maxNum
    

def changeToList(num):
    returnList = []
    while (num != 0):
        returnList.append(num % 10)
        num //= 10

    return returnList[::-1]

def switchIndex(numList, index1, index2):
    numList = copy.deepcopy(numList)
    firstValue= numList[index1]
    secondValue = numList[index2]

    numList[index1] = secondValue
    numList[index2] = firstValue

    return numList

def switchListToStr(numList):
    returnStr = ""

    for num in numList:
        returnStr += str(num)

    return returnStr

def containsDuplicate(numList):
    return len(numList) != len(list(set(numList)))
# num = 32888
# numList = changeToList(num)
#
# print(solution(numList, 2))




T = int(input())
for _ in range(T):
    num, switch = map(int, input().split())
    numList = changeToList(num)
    duplicates = containsDuplicate(numList)
    print("#" + str(_ + 1), end = " ")
    print(solution(numList, switch))