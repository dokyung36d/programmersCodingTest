import sys

def solution():
    N = int(sys.stdin.readline())
    topList = list(map(int, sys.stdin.readline().split()))

    stack = [(topList[0], 0)] ## (Top height, index)
    print(0, end= " ")

    for i in range(1, len(topList)):
        topHeight = topList[i]

        while stack and stack[-1][0] < topHeight:
            stack.pop(-1)

        if stack:
            print(stack[-1][1] + 1, end= " ")
        else:
            print(0, end= " ")
        stack.append((topHeight, i))


solution()