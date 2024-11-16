def solution(n, m, k, userList):
    numAteFish = 0

    userList.sort()

    for i in range(n):
        numAteFish += 1

        if numAteFish > getNumFish(userList[i], m, k):
            return "Impossible"

    return "Possible"
def getNumFish(timeIndex, m, k):
    return (timeIndex // m) * k


T = int(input())

for i in range(1, T + 1):
    n, m, k = map(int, input().split())
    userList = list(map(int, input().split()))

    result = solution(n, m, k, userList)

    print(f"#{i} {result}")