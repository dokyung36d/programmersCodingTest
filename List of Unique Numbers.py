import sys
from collections import deque, defaultdict

def solution():
    N = int(sys.stdin.readline())
    numList = list(map(int, sys.stdin.readline().split()))
    numDict = defaultdict(deque)

    appearDict = defaultdict(int)
    answer = 0
    startIndex = 0
    for i in range(N):
        print(answer)
        if appearDict[numList[i]] == 0:
            answer += i - startIndex + 1
            appearDict[numList[i]] = i + 1
            continue

        startIndex = max(startIndex, appearDict[numList[i]])
        answer += i - startIndex + 1
        appearDict[numList[i]] = i + 1
    return answer


    
    # for i in range(len(numList)):
    #     numDict[numList[i]].append(i)

    # answer = 0
    # startIndex = 0
    # appearDict = defaultdict(int)
    # for i in range(len(numList)):
    #     curNum = numList[i]
    #     if appearDict[curNum] == 0:
    #         answer += i - startIndex + 1
    #         appearDict[curNum] = 1
    #         continue
        
    #     prevSameNumIndex = numDict[curNum].popleft()
    #     if prevSameNumIndex + 1 > startIndex:
    #         startIndex = prevSameNumIndex + 1
        
    #     answer += i - startIndex + 1

    # return answer

print(solution())