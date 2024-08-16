##배달 갈 때에는 끝에서부터 plus해서 cap만큼 배달하기
##수거할 때에도 마찬가지
##만약 list 2개 모두 마지막 부분이 0, 0이면 Pruning하기.

def solution(cap, n, deliveries, pickups):
    answer = -1
    return answer

def get_result_after_round_trip(go_list, back_list, cap, n):
    sum_go = 0
    sum_back = 0
    
    go_index = n - 1
    back_index = n - 1
    
    while sum_go < cap:
        if sum_go + go_list[go_index] < cap:
            sum_go += go_list[go_index]
            go_index -= 1
            
            continue
            
        elif sum_go + go_list[go_index] == cap:
            sum_go += go_list[go_index]
            go_index -= 1
            
            break
            
        else:
            go_list[go_index] -= (cap - sum_go)
            sum_go = cap
            
            break
            
    while sum_back < cap:
        if sum_back + back_list[back_index] < cap:
            sum_back += back_list[back_index]
            back_index -= 1
            
            continue
            
        elif sum_back + back_list[back_index] == cap:
            sum_back += back_list[back_index]
            back_index -= 1
            
            break
            
        else:
            back_list[back_index] -= (cap - sum_back)
            sum_back = cap