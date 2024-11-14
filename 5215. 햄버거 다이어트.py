## https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

import bisect

def removeDescInList(calorieList, scoreList):
    for i in range(len(scoreList) - 1, 0, -1):
        if scoreList[i - 1] > scoreList[i]:
            calorieList.pop(i)
            scoreList.pop(i)

    return calorieList, scoreList



T = int(input())

for _ in range(T):
    N, L = map(int, input().split())

    scoreList = []
    calorieList = []

    score, calorie = map(int, input().split())
    scoreList.append(score)
    calorieList.append(calorie)

    for __ in range(N - 1):
        score, calorie = map(int, input().split())

        index = bisect.bisect_left(calorieList, calorie)

        scoreList.insert(index, score)
        calorieList.insert(index, calorie)

    if calorieList[0] > L:
        print(0)
        continue
    dpCalorie = [0, calorieList[0]]
    dpScore = [0, scoreList[0]]

    for i in range(1, N):
        ##If one food's calorie exceeds L, no need to consider
        if calorieList[i] > L:
            break

        insertList = [(0, 0)]

        for j in range(len(dpCalorie)):
            newCalorie = dpCalorie[j] + calorieList[i]
            newScore = dpScore[j] + scoreList[i]
            if newCalorie > L:
                continue

            index = bisect.bisect_left(insertList, (newCalorie, newScore))
            insertList.insert(index, (newCalorie, newScore))

            # if index < len(dpCalorie) and dpCalorie[index] == newCalorie:
            #     dpScore[index] = max(newScore, dpScore[index])
            #     continue
            # dpCalorie.insert(index, newCalorie)
            # dpScore.insert(index, newScore)

        for k in range(len(insertList)):
            index = bisect.bisect_left(dpCalorie, insertList[k][0])
            if index < len(dpCalorie) and dpCalorie[index] == insertList[k][0]:
                dpScore[index] = max(insertList[k][1], dpScore[index])
                continue
            dpCalorie.insert(index, insertList[k][0])
            dpScore.insert(index, insertList[k][1])


        dpCalorie, dpScore = removeDescInList(dpCalorie, dpScore)
    print(f"#{_ + 1} {dpScore[-1]}")



