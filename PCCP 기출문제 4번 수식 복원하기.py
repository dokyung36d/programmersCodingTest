def solution(expressions):
    maxNum = getMaxNum(expressions)
    candidateList = [i for i in range(maxNum + 1, 10)]
    infoExpressions, solveExpressions= divideExpressions(expressions)

    validCandidateList = validateCandidates(infoExpressions, candidateList)
    return validCandidateList
    
    
    answer = convertXtoTen(5, 8)
    return answer

def validateCandidates(expressions, candidateList):
    validatedCandidateList = []

    for candidate in candidateList:
        if not validateExpressions(expressions, candidate):
            continue
            
        validatedCandidateList.append(candidate)
        
    return validatedCandidateList
    
def validateExpressions(expressions, num):
    for expression in expressions:
        if not decomposeInfoExpression(expression, num):
            return False
        
    return True
        
        
def decomposeInfoExpression(expression, num):
    expression = list(expression.split(" "))
    firstNum = int(expression[0])
    operator = expression[1]
    secondNum = int(expression[2])
    lastNum = int(expression[-1])
    
    firstNumConverted = convertXtoTen(firstNum, num)
    secondNumConverted = convertXtoTen(secondNum, num)
    lastNumConverted = convertXtoTen(lastNum, num)
        
    if operator == "+":
        if firstNumConverted + secondNumConverted == lastNumConverted:
            return True
        return False
    
    if operator == "-":
        if firstNumConverted - secondNumConverted == lastNumConverted:
            return True
        return False
    
def decomposeProblemExpression(expressions):
    pass
    
def divideExpressions(expressions):
    infoExpression = []
    solveExpression = []
    for expression in expressions:
        if expression[-1] == "X":
            solveExpression.append(expression)
            
        else:
            infoExpression.append(expression)
            
    return infoExpression, solveExpression
## 여기서 x는 진법을 의미함
def convertXtoTen(num : int, x : int):
    result = 0
    
    multiplyNum = 1
    while num != 0:
        endNum = num % 10
        result += (multiplyNum * endNum)
        
        multiplyNum *= x
        num = num // 10
        
    return result

def getMaxNum(expressions):
    maxNum = 1
    for expression in expressions:
        infoList = list(expression.split(" "))
        
        for info in infoList:
            try:
                infoInt = int(info)
            except:
                continue
            if int(max(info)) > maxNum:
                maxNum = int(max(info))

    return maxNum
        