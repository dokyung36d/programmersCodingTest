import sys

def solution():
    N, S = map(int, sys.stdin.readline().split())
    numList = list(map(int, sys.stdin.readline().split()))

    start = 1
    end = N
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        result = checkIntervalAvailable(numList, mid, S)

        if result == True:
            end = mid - 1
            answer = mid

        else:
            start = mid + 1
            
    return answer

def checkIntervalAvailable(numList, interval, standard):
    sumValue = getPartSum(numList, 0, interval)

    if sumValue >= standard:
        return True
    
    for i in range(interval, len(numList)):
        deleteNumIndex = i - interval
        addNumIndex = i

        sumValue -= numList[deleteNumIndex]
        sumValue += numList[addNumIndex]

        if sumValue >= standard:
            return True
        
    return False



def getPartSum(numList, startIndex, endIndex):
    # return sum(numList[startIndex:endIndex])

    totalSum = 0
    for i in range(startIndex, endIndex):
        totalSum += numList[i]

    return totalSum




print(solution())