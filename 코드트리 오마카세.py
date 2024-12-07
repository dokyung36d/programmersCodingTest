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
    
    for command in commands:
        if len(command) == 4:
            beltDict = process100(command, beltDict, visitTimeDict, L)

        elif len(command) == 5:
            userList = process200(command, userList)

        elif len(command) == 2:
            process300(command, beltDict, userDict)

    print(beltDict)
    print(visitTimeDict)

def process100(commandList, beltDict, visitTimeDict, L):
    time, place, name = int(commandList[1]), int(commandList[2]), commandList[3]

    visitedTime, visitedPlace =  visitTimeDict[name][0], visitTimeDict[name][1]

    timeGap = visitedTime - time
    placeWhenUserVisited = (place + timeGap) % L

    if len(beltDict[name]) == 0:
        beltDict[name] = [(placeWhenUserVisited, time)]
        return beltDict
    
    index = bisect.bisect_left(beltDict[name], (placeWhenUserVisited, time))
    beltDict[name].insert(index, (placeWhenUserVisited, time))

    return beltDict


def process200(commandList, userList):
    time, place, name, n = int(commandList[0]), int(commandList[1]), commandList[3], int(commandList[4])
    userList.append((time, place, name, n))

    return userList

def process300(commandList, userList, beltDict):
    time = int(commandList[1])
    totalUser = 0
    totalMenus = 0

    for user in userList:
        numUser, numMenus = checkStatusUserInTime(user, time, beltDict)

        totalUser += numUser
        totalMenus += numMenus

    return totalUser, totalMenus

def checkStatusUserInTime(user, checkTime, beltDict, L):
    userVisitedTime, userVisitedPlace, userName, userNum = user[0], user[1], user[2], user[3]

    startIndex = bisect.bisect_left(beltDict[userName], userVisitedPlace)
    for i in range(len(beltDict[userName])):
        currentPlace = beltDict[startIndex - i]

def calculateGap(start, end, length):
    if start >= end:
        return start - end
    
    return (start - 0) + (length - end)


# solution()
print(calculateGap(2, 2, 5))