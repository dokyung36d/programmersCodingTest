##tree문제에서 가지치기 n이 크지 않은 숫자여서 크게 문제 없을 듯
## 평균 취해서 하는 것은 반례 존재

## k번째 층에서는 k번째 주사위의 포함 여부를 결정
## 각 주사위를 선택했을 때의 경우의 수는 dp처럼 결과를 저장, dict 형태로

def solution(dice_list):
    n = len(dice_list)
    bfs_list = [[[0], (n / 2) - 1, get_dict_after_accept_new_dice({}, dice_list[0]), 0], [[], n / 2, {}, 0]]
    ## First Element : List of the dices we chose
    ## Second Element : Number of dices we have to bring
    ## Third Element : All cases of rolling dice
    ## Fourth Element : Layer Depth
    
    winning_record = 0
    winning_combinaion = []
    
    while bfs_list:
        candidate = bfs_list.pop(0)
        depth = candidate[-1] + 1
        
        if depth >= 10:
            continue

        ##First : Accept Dice
        new_candidate = copy_list(candidate)
        
        new_candidate[0].append(depth)
        new_candidate[1] -= 1
        new_candidate[2] = get_dict_after_accept_new_dice(new_candidate[2], dice_list[depth])
        new_candidate[3] = depth
        
        if new_candidate[1] == 0:
            winning_cases = get_winning_cases(new_candidate[0], new_candidate[2], dice_list)
            
            if winning_cases > winning_record:
                winning_record = winning_cases
                winning_combination = new_candidate[0]
        else:
            bfs_list.append(new_candidate)
            
            
        ##Second : Deny Dice
        new_candidate = copy_list(candidate)
        
        remain_dice = 9 - depth
        if remain_dice < new_candidate[1]:
            continue
        new_candidate[3] = depth
        
        bfs_list.append(new_candidate)
        
    return winning_combination
        
        
        
    answer = []
    return answer

def get_dict_after_accept_new_dice(previous_dict : dict, new_dice : list):
    dict_list = []
    
    if len(previous_dict) == 0: ##처음 들어온 주사위인 경우
        total_dict = get_dict_from_single_dice(new_dice)
        
        return total_dict
    
    for number in new_dice:
        new_dict = get_dict_after_accept_new_number(previous_dict = previous_dict, new_number = number)
        dict_list.append(new_dict)
    
    total_dict = sum_dicts(dict_list = dict_list)
    return total_dict
            
def get_dict_after_accept_new_number(previous_dict : dict, new_number : int):
    new_dict = {}
    
    for previous_cases in previous_dict:
        new_cases = previous_cases + new_number
        
        if new_cases not in new_dict:
            new_dict[new_cases] = previous_dict[previous_cases]
        else:
            new_dict[new_cases] += previous_dict[previous_cases]
            
    return new_dict

def sum_dicts(dict_list : list):
    total_dict = {}
    
    for dict in dict_list:
        total_dict = sum_two_dicts(total_dict, dict)
        
    return total_dict
    
def sum_two_dicts(dict1 : dict, dict2 : dict):
    sum_dict = {}
    
    for element1 in dict1:
        if element1 not in sum_dict:
            sum_dict[element1] = dict1[element1]
        else:
            sum_dict[element1] += dict1[element1]
            
    for element2 in dict2:
        if element2 not in sum_dict:
            sum_dict[element2] = dict2[element2]
        else:
            sum_dict[element2] += dict2[element2]
            
    return sum_dict

def get_dict_from_single_dice(dice : list):
    dice_dict = {}
    
    for number in dice:
        if number not in dice_dict:
            dice_dict[number] = 1
        else:
            dice_dict[number] += 1
            
    return dice_dict

def copy_list(original_list):
    copied_list = []
    
    for i in range(len(original_list)):
        copied_list.append(original_list[i])
    
    return copied_list

def get_winning_cases(selected_dice_list : list, dice_result_cases : dict, dice_list : list):
    unselected_dice_list = list(set(range(0, 10)) - set(selected_dice_list))
    unselected_dice_result_cases = {}
    
    for i in range(len(unselected_dice_list)): ## 이 부분
        unselected_dice_result_cases = get_dict_after_accept_new_dice(unselected_dice_result_cases, dice_list[unselected_dice_list[i]])
        
    winning_cases = compare_two_results(dice_result_cases, unselected_dice_result_cases)
    
    return winning_cases

def compare_two_results(result_dict1 : dict, result_dict2 : dict):
    win = 0
    # draw = 0
    # lose = 0
    
    for result1 in result_dict1:
        for result2 in result_dict2:
            if result1 > result2:
                win += result_dict1[result1] * result_dict2[result2]
            # elif result1 == result2:
            #     draw += result_dict1[result1] * result_dict2[result2]
            # elif result1 < result2:
            #     lose += result_dict1[result1] * result_dict2[result2]
    
    return win ## 승리한 경우만 Count 해도 됨.