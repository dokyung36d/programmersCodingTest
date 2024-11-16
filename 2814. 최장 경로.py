from collections import defaultdict

def solution(n, m, infoList):
    answer = 1

    graphDict = makeGraphDict(infoList)

    for i in range(1, n + 1):
        result = dfs(i, graphDict, [], 1)

        if result > answer:
            answer = result

    return answer

def makeGraphDict(infoList):
    graphDict = defaultdict(list)

    for i in range(len(infoList)):
        graphDict[infoList[i][0]].append(infoList[i][1])
        graphDict[infoList[i][1]].append(infoList[i][0])

    return graphDict

def dfs(startPoint, graphDict, visited, length):
    maxLength = length

    flag = 0

    for node in graphDict[startPoint]:
        if node in visited:
            continue
        flag = 1

        newLength = dfs(node, graphDict, visited + [node], length + 1)

        if newLength > maxLength:
            maxLength = newLength

    if flag == 0:
        return 1

    return maxLength


T = int(input())

for i in range(1, T + 1):
    n, m = map(int, input().split())

    infoList = []
    for _ in range(m):
        node1, node2 = map(int, input().split())
        infoList.append((node1, node2))

    result = solution(n, m, infoList)
    print(f"#{i} {result}")