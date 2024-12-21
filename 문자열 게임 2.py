import sys
from collections import defaultdict

def solution():
    W = sys.stdin.readline()
    K = int(sys.stdin.readline())
    W = W[:-1]

    wordDict = defaultdict(list)

    minLength = 10 ** 10
    maxLength = -1

    flag = 0
    for i in range(len(W)):
        alphabet = W[i]
        wordDict[alphabet].append(i)

        if len(wordDict[alphabet]) < K:
            continue
        
        flag = 1
        length = wordDict[alphabet][-1] - wordDict[alphabet][-K] + 1
        if length < minLength:
            minLength = length

        if length > maxLength:
            maxLength = length
        
    if flag == 0:
        print(-1)
        return
    print(minLength, maxLength)




if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        solution()