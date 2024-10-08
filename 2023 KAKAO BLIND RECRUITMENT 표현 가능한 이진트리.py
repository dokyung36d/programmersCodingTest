##일단 숫자 주어지면 이진수로 분해
##이진수로 분해한 list가 2^n - 1 형식이 아니라면 이진수 list 늘리기
##an일 때 왼쪽, 오른쪽 자식은 각각 a2n+1, a2n+2인 사실 이용하기


import math

def solution(numbers):
    return_list = []
    for num in numbers:
        answer = convert_int_to_binary(num)
        answer, depth = make_binary_fit_to_tree(answer, num)
        result = check_parent_available(answer, depth)
        return_list.append(result)
        
    return return_list
    # num = 63
    # answer = convert_int_to_binary(num)
    # answer, depth = make_binary_fit_to_tree(answer, num)
    # answer = check_parent_available(answer, depth)
    # return answer

def convert_int_to_binary(num : int):
    if num == 1:
        return [1, 0]
    log_value_int = int(math.log(num) / math.log(2)) + 1
    binary_list = [] ##2의 경우 -> log(2) = 1 -> [1, 0]으로 표현됨
    
    while log_value_int > -1:
        two_exponential = 2 ** log_value_int
        
        if num < two_exponential:
            log_value_int -= 1
            binary_list.append(0)
            
            continue
        
        num -= two_exponential
        log_value_int -= 1
        binary_list.append(1)
    
    return binary_list[1:]

def make_binary_fit_to_tree(binary_list : list, num):
    binary_list_len = len(binary_list)
    
    if binary_list_len == 1:
        return binary_list_len, 1
    
    required_depth = int(math.log2(binary_list_len + 1))
    
    
    if 2 ** required_depth - 1 == binary_list_len:
        return binary_list, required_depth

    required_depth += 1
    num_zero_insert = 2 ** required_depth - 1 - binary_list_len
    zero_list = [0 for _ in range(num_zero_insert)]
    zero_list.extend(binary_list)
    
    return zero_list, required_depth

def check_parent_available(binary_list, depth):
    n = len(binary_list)
    
    for i in range(1, depth):
        gap = 2 ** i
        start_index = 2 ** (i - 1) - 1
        
        result = check_parent_when_gap_given(binary_list, gap, start_index)
        if result == False:
            return 0
        
    return 1
        
def check_parent_when_gap_given(binary_list, gap, start_index):
    for i in range(start_index, len(binary_list), 2 * gap):
        left_node = binary_list[i]
        right_node = binary_list[i + gap]
        parent_node = binary_list[(2 * i + gap) // 2]
        
        if left_node == 0 and right_node == 0:
            continue
        if parent_node == 0:
            return False
    return True