import math

def solution(numbers):
    num = 59
    answer = convert_int_to_binary(num)
    return answer

def convert_int_to_binary(num : int):
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
    
    return binary_list
        