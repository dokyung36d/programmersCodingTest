from collections import defaultdict
import bisect
import heapq

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

    menuHeap = []
    userDict = {}
    numUser = 0
    numMenu = 0
    
    for command in commands:
        if len(command) == 4:
            menuHeap = process100(command, menuHeap, visitTimeDict, L)
            numMenu += 1

        elif len(command) == 5:
            userDict = process200(command, userDict)
            numUser += 1

        elif len(command) == 2:
            numUserOuted, numUserAte, menuHeap = process300(command, userDict, menuHeap)
            numUser -= numUserOuted
            numMenu -= numUserAte

            print(numUser, numMenu)
            # print(beltDict)

    #     print(beltDict)

    # print(userList)

def process100(commandList, menuHeap, visitTimeDict, L):
    time, place, name = int(commandList[1]), int(commandList[2]), commandList[3]

    visitedTime, visitedPlace =  visitTimeDict[name][0], visitTimeDict[name][1]

    if visitedTime >= time:
        timeGap = visitedTime - time
        placeWhenUserVisited = (place + timeGap) % L
        timeToUserPos = calculateGap(visitedPlace, placeWhenUserVisited, L)
        accessTime = visitedTime + timeToUserPos

    else:
        timeToUserPos = calculateGap(visitedPlace, place, L)
        accessTime = time + timeToUserPos

    heapq.heappush(menuHeap, (accessTime, name))

    # if len(beltDict[name]) == 0:
    #     beltDict[name] = [accessTime]
    #     return beltDict
    
    # index = bisect.bisect_left(beltDict[name], accessTime)
    # beltDict[name].insert(index, accessTime)

    return menuHeap


def process200(commandList, userDict):
    time, place, name, n = int(commandList[1]), int(commandList[2]), commandList[3], int(commandList[4])
    userDict[name] = n

    return userDict

def process300(commandList, userDict, menuHeap):
    time = int(commandList[1])
    totalNumUserOuted, totalNumUserAte, menuHeap = checkStatusUserInTime(time, menuHeap, userDict)

    # for i in range(len(userList) - 1, -1, -1):
    #     user = userList[i]
    #     userOuted, numAteMenus, beltDict = checkStatusUserInTime(user, time, beltDict, L)
    #     totalNumUserOuted += userOuted
    #     totalNumUserAte += numAteMenus

    #     if userOuted == 1:
    #         userList.pop(i)
    #         continue

    #     userList[i] = (user[0], user[1], user[2], user[3] - numAteMenus)

    return totalNumUserOuted, totalNumUserAte, menuHeap

def checkStatusUserInTime(checkTime, menuHeap, userDict):
    numAteMenu = 0
    numUserOuted = 0

    while menuHeap:
        menuArrivedTime, menuOwner = heapq.heappop(menuHeap)

        if menuArrivedTime > checkTime:
            heapq.heappush(menuHeap, (menuArrivedTime, menuOwner))
            break

        numAteMenu += 1
        userDict[menuOwner] -= 1

        if userDict[menuOwner] == 0:
            numUserOuted += 1


    
    return numUserOuted, numAteMenu, menuHeap

        


def calculateGap(start, end, length):
    if start >= end:
        return start - end
    
    return (start - 0) + (length - end)


solution()
# print(calculateGap(3, 1, 5))