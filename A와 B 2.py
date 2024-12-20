import sys

def solution():
    S = sys.stdin.readline()
    T = sys.stdin.readline()

    S = S[:-1]
    T = T[:-1]


    queue = [T]

    while queue:
        string = queue.pop()

        if string == S:
            return 1
        
        if len(string) == len(S):
            continue

        if string[-1] == "A":
            queue.append(string[:-1])

        if string[0] == "B":
            queue.append(string[:0:-1])

    return 0

    # numBInS = countB(S)
    # numBInT = countB(T)

    # queue = [(S, numBInS)]

    # while queue:
    #     string, numB = queue.pop(0)

    #     if len(string) == len(T):
    #         continue

    #     firstOperationResult = firstOperation(string)
    #     if (numBInT - numB) % 2 == 0 and firstOperationResult in T:
    #         queue.append((firstOperationResult, numB))


    #     secondOperationResult = secondOperation(string)
        


def countB(string):
    num = 0

    for i in range(len(string)):
        if string[i] == "B":
            num += 1


    return num

def firstOperation(string):
    return string + "A"

def secondOperation(string):
    newString = string + "B"

    return newString[::-1]

print(solution())