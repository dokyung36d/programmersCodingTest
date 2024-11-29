def solution(expressions):
    maxNum = getMaxNum(expressions)
    candidateList = [i for i in range(maxNum + 1, 10)]
    infoExpressions, solveExpressions= divideExpressions(expressions)

    validCandidateList = validateCandidates(infoExpressions, candidateList)
    
    answerList = [] 
    for solveExpression in solveExpressions:
        result = getSolveProblem(solveExpression, validCandidateList)
        answerList.append(result)
        
    return answerList
    
    
    answer = convertXtoTen(5, 8)
    return answer

def getSolveProblem(expression, validCandidateList):
    flag = 0
    base = decomposeProblemExpression(expression, validCandidateList[0])
    baseConverted = convertTentoX(base, validCandidateList[0])
    
    for i in range(1, len(validCandidateList)):
        result = decomposeProblemExpression(expression, validCandidateList[i])
        resultConverted = convertTentoX(result, validCandidateList[i])
        
        if resultConverted != baseConverted:
            flag = 1
            break
            
    if flag == 0:
        return expression[:-1] + str(baseConverted)
    else:
        return expression[:-1] + "?"
            

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
    
def decomposeProblemExpression(expression, num):
    expression = list(expression.split(" "))
    firstNum = int(expression[0])
    operator = expression[1]
    secondNum = int(expression[2])
    
    firstNumConverted = convertXtoTen(firstNum, num)
    secondNumConverted = convertXtoTen(secondNum, num)

    if operator == "+":
        return firstNumConverted + secondNumConverted
    
    if operator == "-":
        return firstNumConverted - secondNumConverted
    
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

def convertTentoX(num : int, x : int):
    result = 0
    
    multiplyNum = 1
    while num != 0:
        endNum = num % x
        result += (multiplyNum * endNum)
        
        multiplyNum *= 10
        num = num // x
        
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