import sys
from itertools import combinations
import heapq

def solution(num):
    numList = [str(i) for i in range(1, num + 1)]
    operatorIndices = [i for i in range(num - 1)]
    possibleCases = []
    answerHeap = []
    
    for i in range(0, num - 1):
        blankCombinations = list(combinations(operatorIndices, i))
        appliedBlankList = getPossibleCasesWhenBlankIsGiven(numList, blankCombinations)
        for appliedBlank in appliedBlankList:
            cases = getPossibleCases(appliedBlank)
            for case in cases:
                possibleCases.append((appliedBlank, case))

    for i in range(len(possibleCases)):
        appliedBlank, operator = possibleCases[i][0], possibleCases[i][1]
        heapq.heappush(answerHeap, changeToAnswerFormat(appliedBlank, operator))

    while answerHeap:
        print(heapq.heappop(answerHeap))

def changeToAnswerFormat(appliedBlank, operator):
    appliedBlank = appliedBlank[:]
    for i in range(len(appliedBlank)):
        if len(str(appliedBlank[i])) == 1:
            continue

        newString = ""
        for j in range(len(str(appliedBlank[i]))):
            newString += str(appliedBlank[i])[j]
            newString += " "
        newString = newString[:-1]
        appliedBlank[i] = newString

    answerFormat = ""
    for i in range(len(operator)):
        answerFormat += str(appliedBlank[i])
        answerFormat += operator[i]

    answerFormat += str(appliedBlank[-1])
    return answerFormat


def getPossibleCases(appliedBlank : list):
    queue = [(appliedBlank, [])]
    returnList = []

    while queue:
        node = queue.pop()
        numList, prevOperator = node[0], node[1]

        if len(numList) == 2:
            if numList[0] == numList[1]:
                returnList.append(prevOperator + ["-"])
            elif numList[0] == -numList[1]:
                returnList.append(prevOperator + ["+"])
            
            continue

            
        
        firstOperand, secondOperand = numList[0], numList[1]
        newList = [firstOperand + secondOperand] + numList[2:]
        queue.append((newList, prevOperator + ["+"]))
        
        newList = [firstOperand - secondOperand] + numList[2:]
        queue.append((newList, prevOperator + ["-"]))

    return returnList


        
def getPossibleCasesWhenBlankIsGiven(numList, blankCombinations):
    returnList = []
    for blankCombination in blankCombinations:
        numListAppliedBlank = makeNumList(numList, blankCombination)
        if not checkPossible(numListAppliedBlank):
            continue
            
        returnList.append(numListAppliedBlank)

    return returnList

def checkPossible(numList):
    if 2 * max(numList) <= sum(numList):
        return True
    
    return False

def makeNumList(numList, blankIndices):
    stack = []

    for i in range(len(numList) - 1, -1, -1):
        newString = numList[i]
        if i in blankIndices:
            tailString = stack.pop()
            newString += tailString

        stack.append(newString)

    
    returnList = []
    while stack:
        returnList.append(int(stack.pop()))


    return returnList

N = int(sys.stdin.readline())

for _ in range(N-1):
    num = int(sys.stdin.readline())
    solution(num)
    print()

num = int(sys.stdin.readline())
solution(num)