import sys
import bisect

def solution():
    N = int(sys.stdin.readline())
    liquidList = list(map(int, sys.stdin.readline().split()))

    zeroIndex = bisect.bisect_left(liquidList, 0)

    answer = 10 ** 10
    answerCombination = []
    

    # Negative Case
    for i in range(N):
        value = liquidList[i]
        swappedValue = swapNum(value)

        similarValueIndex = bisect.bisect_left(liquidList, swappedValue)

        if checkIndex(similarValueIndex, N) and i != similarValueIndex and abs(value + liquidList[similarValueIndex]) < answer:
            answer = abs(value + liquidList[similarValueIndex])
            answerCombination = [value, liquidList[similarValueIndex]]

        if checkIndex(similarValueIndex - 1, N) and i != similarValueIndex - 1 and abs(value + liquidList[similarValueIndex - 1]) < answer:
            answer = abs(value + liquidList[similarValueIndex - 1])
            answerCombination = [value, liquidList[similarValueIndex - 1]]


    # ## Positive Case
    # for i in range(zeroIndex, N):
    #     positiveValue = liquidList[i]
    #     swappedPositiveValue = -positiveValue

    #     similarValueIndex = bisect.bisect_left()


    print(min(answerCombination), max(answerCombination))

def swapNum(num):
    return -num


def checkIndex(index, N):
    if 0 <= index < N:
        return True
    
    return False
solution()