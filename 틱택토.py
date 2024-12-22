import sys


def solution():
    while True:
        string = sys.stdin.readline()
        string = string[:-1]

        if len(string) == 3:
            return
        
        matrix = changeStringToMatrix(string)

        if checkValid(matrix):
            print("valid")

        else:
            print("invalid")
        
def checkValid(matrix):
    numX, numO = getXONum(matrix)
    
    ##Case 1: Draw
    if not containBlank(matrix) and numX == numO + 1 and not checkBingo(matrix, ["X", "O"]):
        return True
    
    ##Case 2: X win
    if numX == numO + 1 and checkBingo(matrix, ["X"]) and not checkBingo(matrix, ["O"]):
        return True
    
    ##Case 3: O win
    if numX == numO and checkBingo(matrix, ["O"]) and not checkBingo(matrix, ["X"]):
        return True
    
    return False
    
def containBlank(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == ".":
                return True
            
    return False
    

def checkBingo(matrix, targets):
    ##Check width and Height
    for i in range(3):
        rowValueList = [matrix[i][j] for j in range(3)]
        if len(list(set(rowValueList))) == 1 and rowValueList[0] in targets:
            return True
        
        colValueList = [matrix[j][i] for j in range(3)]
        if len(list(set(colValueList))) == 1 and colValueList[0] in targets:
            return True
    
    ##Check Diag
    diagList = [matrix[i][i] for i in range(3)]
    if len(list(set(diagList))) == 1 and diagList[0] in targets:
        return True
    
    swapList = [matrix[i][2 - i] for i in range(3)]
    if len(list(set(swapList))) == 1 and swapList[0] in targets:
        return True
    

    return False

def getXONum(matrix):
    numO, numX = 0, 0

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == "O":
                numO += 1

            if matrix[i][j] == "X":
                numX += 1


    return numX, numO
    
    # if numX == numO or numX == numO + 1:
    #     return True
    
    # return False
        

def changeStringToMatrix(string):
    matrix = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(9):
        matrix[i // 3][i % 3] = string[i]

    return matrix


solution()