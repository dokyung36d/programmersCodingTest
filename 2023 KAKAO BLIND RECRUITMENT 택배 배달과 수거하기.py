##배달 갈 때에는 끝에서부터 plus해서 cap만큼 배달하기
##수거할 때에도 마찬가지
##만약 list 2개 모두 마지막 부분이 0, 0이면 Pruning하기.

##[1, 0, 2, 0, 1, 0, 2]
##[0, 2, 0, 1, 0, 2, 0]

import sys
sys.setrecursionlimit(10**7)

def solution(cap, n, deliveries, pickups):
    result = get_result_after_round_trip(deliveries, pickups, n - 1, n - 1, cap, n, 0)

    return result

sum_list = []

def get_result_after_round_trip(go_list, back_list, go_index, back_index, cap, n, sum_distance):
    global sum_list
    if go_index == -2 and back_index == -2:
        return sum_distance
    
    sum_go = 0
    sum_back = 0
    
    sum_distance += (2 * max([go_index + 1, back_index + 1]))
    # sum_list.append(2 * max([go_index + 1, back_index + 1]))
    
    while sum_go < cap and go_index >= -1:
        if (sum_go + go_list[go_index]) < cap:
            sum_go += go_list[go_index]
            go_index -= 1
            
            continue
            
        elif (sum_go + go_list[go_index]) == cap:
            sum_go += go_list[go_index]
            go_index = get_prev_index_which_not_zero(go_list, go_index)
            
            break
            
            
        else:
            go_list[go_index] -= (cap - sum_go)
            sum_go = cap
            
            break
            
    while sum_back < cap and back_index >= -1:
        if sum_back + back_list[back_index] < cap:
            sum_back += back_list[back_index]
            back_index -= 1
            
            continue
            
        elif sum_back + back_list[back_index] == cap:
            sum_back += back_list[back_index]
            back_index = get_prev_index_which_not_zero(back_list, back_index)
            
            break
            
        else:
            back_list[back_index] -= (cap - sum_back)
            sum_back = cap
            
            break
            
    return get_result_after_round_trip(go_list, back_list, go_index, back_index, cap, n, sum_distance)

def get_prev_index_which_not_zero(list1 : list, index):
    if index == 0:
        return -2
    index -= 1
    
    while index >= 0:
        if list1[index] != 0:
            return index
        index -= 1
        
    return -2
    