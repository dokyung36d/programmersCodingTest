import copy


def solution(numList, switchNum, answer = ""):
    if switchNum == 0:
        answer += switchListToStr(numList)
        return answer

    if len(numList) == 2:
        if switchNum >= 2:
            answer += str(numList[0])
            answer += str(numList[1])

        else:
            answer += str(numList[1])
            answer += str(numList[0])

        return answer

    maxNum = max(numList)
    maxNumIndex = len(numList) - numList[::-1].index(maxNum) - 1

    index = 0
    while index != maxNumIndex:
        if numList[index] != maxNum:
            break

        index += 1

    ## maxNum 앞의 값들이 전부 maxNum인 경우
    if index == maxNumIndex:
        return solution(numList[1:], switchNum, answer + str(numList[0]))

    numList = switchIndex(numList, index, maxNumIndex)
    return solution(numList[1:], switchNum - 1, answer + str(numList[0]))

def changeToList(num):
    returnList = []
    while (num != 0):
        returnList.append(num % 10)
        num //= 10

    return returnList[::-1]

def switchIndex(numList, index1, index2):
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

# num = 757148
# numList = changeToList(num)
#
# print(solution(numList, 1))

def handleMatchCase(numlist, switch):
    sorted_list =copy.deepcopy(numlist)
    sorted_list.sort()




T = int(input())
for _ in range(T):
    num, switch = map(int, input().split())
    numList = changeToList(num)
    print(solution(numList, switch))