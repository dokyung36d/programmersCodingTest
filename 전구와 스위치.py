import sys
import heapq

def solution():
    N = int(sys.stdin.readline())
    curCondition = sys.stdin.readline()
    destCondition = sys.stdin.readline()

    curCondition = curCondition[:-1]
    destCondition = destCondition[:-1]

    queue = []
    if curCondition[0] == destCondition[0]:
        heapq.heappush(queue, (0, [0, 0, 0], 0)) ##curIndex, switch Status(-1, 0, 1), totalNumSwitchOn
        heapq.heappush(queue, (0, [0, 1, 1], 2))
    else:
        heapq.heappush(queue, (0, [0, 0, 1], 1))
        heapq.heappush(queue, (0, [0, 1, 0], 1))


    while queue:
        node = heapq.heappop(queue)
        prevIndex, prevSwitch, totalNumSwitchOn = node[0], node[1], node[2]

        curIndex = prevIndex + 1
        if sum(prevSwitch[1:]) % 2 == 0:
            switchChanged = 0
        else:
            switchChanged = 1
        
        
        if curCondition[curIndex] == destCondition[curIndex]:
            needToChangeSwtich = 0
        else:
            needToChangeSwtich = 1

        
        if (switchChanged and needToChangeSwtich) or (not switchChanged and not needToChangeSwtich):
            switchOn = 0
        else:
            switchOn = 1


        if curIndex == N - 1 and switchOn == 0:
            return totalNumSwitchOn

        if curIndex != N - 1:
            heapq.heappush(queue, (curIndex, prevSwitch[1:] + [switchOn], totalNumSwitchOn + switchOn))
            
    return -1

print(solution())