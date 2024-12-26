import sys

def solution():
    n = int(sys.stdin.readline())
    answer = 0

    stack = []
    xPos, height = map(int, sys.stdin.readline().split())
    stack.append((xPos, height))  

    for _ in range(n - 1):
        newXPos, newHeight = map(int, sys.stdin.readline().split())
        if len(stack) == 0:
            stack.append((newXPos, newHeight))
            continue
        
        while stack:
            prevXPos, prevHeight = stack.pop()

            if prevHeight < newHeight:
                stack.append((prevXPos, prevHeight))
                break

            elif prevHeight == newHeight:
                break

            elif prevHeight > newHeight:
                answer += 1

        if newHeight != 0:
            stack.append((newXPos, newHeight))
    
    for i in range(len(stack)):
        if stack[i][1] != 0:
            answer += 1

    return answer

print(solution())