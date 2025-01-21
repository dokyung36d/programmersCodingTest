import sys
from collections import defaultdict

n = int(sys.stdin.readline())
aList = []
bList = []
cList = []
dList = []


for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())

    aList.append(a)
    bList.append(b)
    cList.append(c)
    dList.append(d)
    

secondDict = defaultdict(int)
for c in cList:
    for d in dList:
        secondDict[c + d] += 1



answer = 0
for a in aList:
    for b in bList:
        value = - (a + b)
        if value in secondDict:
            answer += secondDict[-(a + b)]
        

print(answer)