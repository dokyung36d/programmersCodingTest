import sys
from collections import defaultdict

def solution():
    N = int(sys.stdin.readline())
    edgeDict = defaultdict(int)
    answerDict = defaultdict(int)

    for i in range(1, N + 1):
        dest = int(sys.stdin.readline())
        edgeDict[i] = dest

    for i in range(1, N + 1):
        if answerDict[i] == 1:
            continue

        visited = dfs(i, edgeDict[i], [i], edgeDict)

        for j in range(len(visited)):
            answerDict[visited[j]] = 1


    keyList = sorted(answerDict.keys())
    numValid = 0
    validKeyList = []

    for key in keyList:
        if answerDict[key] == 1:
            numValid += 1
            validKeyList.append(key)

    
    print(numValid)
    for valid in validKeyList:
        print(valid)

def dfs(startPos, currentPos, visited, edgeDict):
    if startPos == currentPos:
        return visited
    
    if currentPos in visited:
        return []
    
    return dfs(startPos, edgeDict[currentPos], visited + [currentPos], edgeDict)


solution()