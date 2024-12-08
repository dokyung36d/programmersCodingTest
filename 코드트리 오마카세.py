from collections import defaultdict
import bisect

def solution():
    L, Q = map(int, input().split())

    beltDict = defaultdict(list)
    userDict = defaultdict(list)
    visitTimeDict = {}
    commands = []

    for _ in range(Q):
        commandList = list(input().split())

        if commandList[0] == "200":
            visitTimeDict[commandList[3]] = (int(commandList[1]), int(commandList[2]))

        commands.append(commandList)

    userList = []
    numUser = 0
    numMenu = 0
    
    for command in commands:
        if len(command) == 4:
            beltDict = process100(command, beltDict, visitTimeDict, L)
            numMenu += 1

        elif len(command) == 5:
            userList = process200(command, userList)
            numUser += 1

        elif len(command) == 2:
            beltDict, numUserOuted, numUserAte = process300(command, userList, beltDict, L)
            numUser -= numUserOuted
            numMenu -= numUserAte

            print(numUser, numMenu)
            # print(beltDict)

    #     print(beltDict)

    # print(userList)

def process100(commandList, beltDict, visitTimeDict, L):
    time, place, name = int(commandList[1]), int(commandList[2]), commandList[3]

    visitedTime, visitedPlace =  visitTimeDict[name][0], visitTimeDict[name][1]

    timeGap = visitedTime - time
    placeWhenUserVisited = (place + timeGap) % L
    timeToUserPos = calculateGap(visitedPlace, placeWhenUserVisited, L)

    if len(beltDict[name]) == 0:
        beltDict[name] = [(timeToUserPos, time)]
        return beltDict
    
    index = bisect.bisect_left(beltDict[name], (timeToUserPos, time))
    beltDict[name].insert(index, (timeToUserPos, time))

    return beltDict


def process200(commandList, userList):
    time, place, name, n = int(commandList[1]), int(commandList[2]), commandList[3], int(commandList[4])
    userList.append((time, place, name, n))

    return userList

def process300(commandList, userList, beltDict, L):
    time = int(commandList[1])
    totalNumUserOuted = 0
    totalNumUserAte = 0

    for i in range(len(userList) - 1, -1, -1):
        user = userList[i]
        userOuted, numAteMenus, beltDict = checkStatusUserInTime(user, time, beltDict, L)
        totalNumUserOuted += userOuted
        totalNumUserAte += numAteMenus

        if userOuted == 1:
            userList.pop(i)
            continue

        userList[i] = (user[0], user[1], user[2], user[3] - numAteMenus)

    return beltDict, totalNumUserOuted, totalNumUserAte

def checkStatusUserInTime(user, checkTime, beltDict, L):
    userVisitedTime, userVisitedPlace, userName, MaxNumUserEat = user[0], user[1], user[2], user[3]

    numAteMenu = 0
    userOuted = 0

    ## 손님이 방문하기 전이면 의미 없음
    if userVisitedTime > checkTime:
        return 0, 0
    
    allowedTime = checkTime - userVisitedTime

    ateMenuIndices = []    
    for i in range(len(beltDict[userName])):
        timeToSpent = beltDict[userName][i][0]

        if timeToSpent > allowedTime:
            break

        numAteMenu += 1
        ateMenuIndices.append(i)
        if numAteMenu >= MaxNumUserEat:
            break

    for i in range(len(ateMenuIndices) - 1, -1, -1):
        beltDict[userName].pop(ateMenuIndices[i])
    
    if len(beltDict[userName]) == 0:
        userOuted = 1
        del beltDict[userName]

    
    return userOuted, numAteMenu, beltDict

        


def calculateGap(start, end, length):
    if start >= end:
        return start - end
    
    return (start - 0) + (length - end)


solution()
# print(calculateGap(3, 1, 5))