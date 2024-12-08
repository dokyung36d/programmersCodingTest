from collections import defaultdict
import bisect

def solution():
    L, Q = map(int, input().split())

    beltDict = defaultdict(list)
    ateDict = defaultdict(int)
    visitTimeDict = defaultdict(int)
    commands = []

    # for _ in range(Q):
    #     commandList = list(input().split())

    #     if commandList[0] == "200":
    #         visitTimeDict[commandList[3]] = (int(commandList[1]), int(commandList[2]))

    #     commands.append(commandList)

    userList = []
    numUser = 0
    numMenu = 0
    for _ in range(Q):
        command = list(input().split())

        if len(command) == 4:
            beltDict = process100(command, beltDict, visitTimeDict, L)
            numMenu += 1

        elif len(command) == 5:
            userList, beltDict, visitTimeDict = process200(command, userList, beltDict, visitTimeDict, L)
            numUser += 1

        elif len(command) == 2:
            beltDict, numUserOuted, numUserAte = process300(command, userList, beltDict, L, ateDict)
            numUser -= numUserOuted
            numMenu -= numUserAte

            print(numUser, numMenu)
            # print(beltDict)

    #     print(beltDict)

    # print(userList)

def process100(commandList, beltDict, visitTimeDict, L):
    time, place, name = int(commandList[1]), int(commandList[2]), commandList[3]

    if visitTimeDict[name] == 0:
        beltDict[name].append((time, place))
        return beltDict

    visitedTime, visitedPlace =  visitTimeDict[name][0], visitTimeDict[name][1]

    if visitedTime >= time:
        timeGap = visitedTime - time
        placeWhenUserVisited = (place + timeGap) % L
        timeToUserPos = calculateGap(visitedPlace, placeWhenUserVisited, L)
        accessTime = visitedTime + timeToUserPos

    else:
        timeToUserPos = calculateGap(visitedPlace, place, L)
        accessTime = time + timeToUserPos

    if len(beltDict[name]) == 0:
        beltDict[name] = [accessTime]
        return beltDict
    
    index = bisect.bisect_left(beltDict[name], accessTime)
    beltDict[name].insert(index, accessTime)

    return beltDict


def process200(commandList, userList, beltDict, visitTimeDict, L):
    time, place, name, n = int(commandList[1]), int(commandList[2]), commandList[3], int(commandList[4])
    userList.append((time, place, name, n))

    visitTimeDict[name] = (time, place)
    beltDict = updateBeltDict(visitTimeDict, beltDict, name, L)
    return userList, beltDict, visitTimeDict

def process300(commandList, userList, beltDict, L, ateDict):
    time = int(commandList[1])
    totalNumUserOuted = 0
    totalNumUserAte = 0

    for i in range(len(userList) - 1, -1, -1):
        user = userList[i]
        userOuted, numAteMenus, beltDict = checkStatusUserInTime(user, time, beltDict, L, ateDict)
        totalNumUserOuted += userOuted
        totalNumUserAte += numAteMenus

        if userOuted == 1:
            userList.pop(i)
            continue

        userList[i] = (user[0], user[1], user[2], user[3] - numAteMenus)

    return beltDict, totalNumUserOuted, totalNumUserAte

def checkStatusUserInTime(user, checkTime, beltDict, L, ateDict):
    userVisitedTime, userVisitedPlace, userName, maxNumUserEat = user[0], user[1], user[2], user[3]

    ## 손님이 방문하기 전이면 의미 없음
    if userVisitedTime > checkTime:
        return 0, 0, beltDict

    index = bisect.bisect_right(beltDict[userName], checkTime)
    numEat = index - ateDict[userName]
    if numEat < maxNumUserEat:
        ateDict[userName] += numEat
        return 0, numEat, beltDict
    
    # beltDict[userName] = beltDict[userName][:maxNumUserEat]
    del beltDict[userName]
    return 1, maxNumUserEat, beltDict

        


def calculateGap(start, end, length):
    if start >= end:
        return start - end
    
    return (start - 0) + (length - end)

def updateBeltDict(visitTimeDict, beltDict, name, L):
    visitedTime, visitedPlace = visitTimeDict[name][0], visitTimeDict[name][1]

    updatedList = []
    for i in range(len(beltDict[name])):
        time, place =beltDict[name][i][0], beltDict[name][i][1]

        if visitedTime >= time:
            timeGap = visitedTime - time
            placeWhenUserVisited = (place + timeGap) % L
            timeToUserPos = calculateGap(visitedPlace, placeWhenUserVisited, L)
            accessTime = visitedTime + timeToUserPos

        else:
            timeToUserPos = calculateGap(visitedPlace, place, L)
            accessTime = time + timeToUserPos


        if len(updatedList) == 0:
            updatedList.append(accessTime)
            continue
        
        index = bisect.bisect_left(updatedList, accessTime)
        updatedList.insert(index, accessTime)

    beltDict[name] = updatedList

    return beltDict
solution()
# print(calculateGap(3, 1, 5))