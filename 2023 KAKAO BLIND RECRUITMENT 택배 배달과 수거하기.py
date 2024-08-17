##배달 갈 때에는 끝에서부터 plus해서 cap만큼 배달하기
##수거할 때에도 마찬가지
##만약 list 2개 모두 마지막 부분이 0, 0이면 Pruning하기.

##[1, 0, 2, 0, 1, 0, 2]
##[0, 2, 0, 1, 0, 2, 0]

import sys
import copy
sys.setrecursionlimit(10**7)

def solution(cap, n, deliveries, pickups):
    result = get_result_after_round_trip(deliveries, pickups, n - 1, n - 1, cap, n, 0)

    return result


def get_result_after_round_trip(go_list, back_list, go_index, back_index, cap, n, sum_distance):
    if go_index == -1 and back_index == -1:
        return sum_distance
    
    sum_go = 0
    sum_back = 0
    
    flag = 0
    
    if go_list[go_index] == 0 and back_list[back_index] == 0:
        go_index = get_prev_index_which_not_zero(go_list, go_index)
        back_index = get_prev_index_which_not_zero(back_list, back_index)

    sum_distance += (2 * max([go_index + 1, back_index + 1]))
        
    while sum_go < cap and go_index >= 0:
        if (sum_go + go_list[go_index]) < cap:
            sum_go += go_list[go_index]
            go_index = get_prev_index_which_not_zero(go_list, go_index)
            
            continue
            
        elif (sum_go + go_list[go_index]) == cap:
            sum_go += go_list[go_index]
            go_index = get_prev_index_which_not_zero(go_list, go_index)
            
            break
            
            
        else:
            go_list[go_index] -= (cap - sum_go)
            sum_go = cap
            
            if go_list[go_index] // cap > 2:
                flag = 1
            
            break
            
    while sum_back < cap and back_index >= 0:
        if sum_back + back_list[back_index] < cap:
            sum_back += back_list[back_index]
            back_index = get_prev_index_which_not_zero(back_list, back_index)
            
            continue
            
        elif sum_back + back_list[back_index] == cap:
            sum_back += back_list[back_index]
            back_index = get_prev_index_which_not_zero(back_list, back_index)
            
            break
            
        else:
            back_list[back_index] -= (cap - sum_back)
            sum_back = cap
            
            if back_list[back_index] // cap > 2 and flag == 1:
                go_list, back_list, go_index, back_index, sum_distance = process_hot_place(go_list, back_list, go_index, back_index, cap, sum_distance)
                
            
            break
            
    return get_result_after_round_trip(go_list, back_list, go_index, back_index, cap, n, sum_distance)

def process_hot_place(list1, list2, index1, index2, cap, sum_distance):
    num_iteration = min([list1[index1] // cap, list2[index2] // cap])
    sum_distance += num_iteration * (2 * max([index1 + 1, index2 + 1]))

    list1[index1] -= cap * num_iteration
    list2[index2] -= cap * num_iteration
    
    if list1[index1] == 0:
        index1 = get_prev_index_which_not_zero(list1, index1)
    if list2[index2] == 0:
        index2 = get_prev_index_which_not_zero(list2, index2)
        
    return (list1, list2, index1, index2, sum_distance)

def get_prev_index_which_not_zero(list1 : list, index):
    if index == 0:
        return -1

    index -= 1
    
    while index >= 0:
        if list1[index] != 0:
            return index
        index -= 1
        
    return -1
    