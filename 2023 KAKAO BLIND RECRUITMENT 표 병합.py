## merge table에서 만약 있으면 각 element는 tuple 형식

##	실행한 결괏값 "UNMERGE 1 4"이 기댓값 ["EMPTY","group"]과 다릅니다.

import copy

def solution(commands):
    value_table = [[0 for _ in range(50)] for _ in range(50)]
    merge_table = [[[] for _ in range(50)] for _ in range(50)]
    
    return_list = []
    
    for command in commands:
        value_table, merge_table = process_instruction(command, value_table, merge_table, return_list)
        
#         try:
#             value_table, merge_table = process_instruction(command, value_table, merge_table, return_list)
        
#         except Exception as E:
#             return str(E)
    return return_list

def process_instruction(command, value_table, merge_table, return_list):
    command_tuple = command.split(" ")
    
    if command_tuple[0] == "UPDATE" and len(command_tuple) == 4:
        indices = (int(command_tuple[1]) - 1, int(command_tuple[2]) - 1)
        value = command_tuple[3]
        
        value_table, merge_table = update_by_location(value_table, merge_table, indices, value)
        
        return value_table, merge_table
    
    if command_tuple[0] == "UPDATE" and len(command_tuple) == 3:
        value_table = update_by_value(value_table, origin_value = command[1], change_value = command[2])
        
        return value_table, merge_table
    
    if command_tuple[0] == "MERGE":
        indices_1 = (int(command_tuple[1]) - 1, int(command_tuple[2]) - 1)
        indices_2 = (int(command_tuple[3]) - 1, int(command_tuple[4]) - 1)
        
        value_table, merge_table = merge(value_table, merge_table, indices_1, indices_2)
        
        return value_table, merge_table
    
    if command_tuple[0] == "UNMERGE":
        indices = (int(command_tuple[1]) - 1, int(command_tuple[2]) - 1)
        value_table, merge_table = unmerge(value_table, merge_table, indices)
        
        return value_table, merge_table
    
    if command_tuple[0] == "PRINT":
        indices = (int(command_tuple[1]) - 1, int(command_tuple[2]) - 1)
        result = print_func(value_table, indices)
        
        return_list.append(result)
        
        return value_table, merge_table
    
    return command_tuple

def update_by_location(value_table, merge_table, indices : tuple, value):
    if merge_table[indices[0]][indices[1]] == [indices]:
        value_table[indices[0]][indices[1]] = value
        
        return value_table, merge_table
    
    
    elif merge_table[indices[0]][indices[1]] == []:
        value_table[indices[0]][indices[1]] = value
        merge_table[indices[0]][indices[1]] = [indices]
        
        return value_table, merge_table
    
    for merged_indices in merge_table[indices[0]][indices[1]]:
        value_table[merged_indices[0]][merged_indices[1]] = value
        
    return value_table, merge_table

def update_by_value(value_table, origin_value, change_value): ##Need Refactoring
    for i in range(50):
        for j in range(50):
            if value_table[i][j] == origin_value:
                value_table[i][j] = change_value
                
    return value_table

def merge(value_table, merge_table, indices_1, indices_2): ##merge -> [] 이면 value는 0, 그러나 역은 성립 X
    merge = merge_table[indices_1[0]][indices_1[1]]
    
    if merge_table[indices_1[0]][indices_1[1]] == [] and merge_table[indices_2[0]][indices_2[1]] == []: ##태초의 상태
        merge = [indices_1, indices_2]
        merge_table[indices_1[0]][indices_1[1]] = merge
        merge_table[indices_2[0]][indices_2[1]] = merge
        
        return value_table, merge_table
    
    if value_table[indices_1[0]][indices_1[1]] == 0 and value_table[indices_2[0]][indices_2[1]] != 0:
        merge_table[indices_2[0]][indices_2[1]].extend(merge_table[indices_1[0]][indices_1[1]])
        
        for merged in merge_table[indices_1[0]][indices_1[1]]:
            value_table[merged[0]][merged[1]] = value_table[indices_2[0]][indices_2[1]]
            
        merge_table[indices_1[0]][indices_1[1]] = merge_table[indices_2[0]][indices_2[1]]
        value_table[indices_1[0]][indices_1[1]] = value_table[indices_2[0]][indices_2[1]]
        
        return value_table, merge_table
    
    if value_table[indices_1[0]][indices_1[1]] != 0:
        merge_table[indices_1[0]][indices_1[1]].extend(merge_table[indices_2[0]][indices_2[1]])
        
        for merged in merge_table[indices_2[0]][indices_2[1]]:
            value_table[merged[0]][merged[1]] = value_table[indices_1[0]][indices_1[1]]
            
        merge_table[indices_2[0]][indices_2[1]] = merge_table[indices_1[0]][indices_1[1]]
        value_table[indices_2[0]][indices_2[1]] = value_table[indices_1[0]][indices_1[1]]
        
        return value_table, merge_table

    
    merge.extend(merge_table[indices_2[0]][indices_2[1]])
    for indices in merge_table[indices_2[0]][indices_2[1]]: ##합칠 때 여러 개일 경우 value 값도 다 변경해줘야 함
        value_table[indices[0]][indices[1]] = value_table[indices_1[0]][indices_1[1]]
        merge_table[indices[0]][indices[1]] = merge
    
    merge_table[indices_1[0]][indices_1[1]] = merge
    merge_table[indices_2[0]][indices_2[1]] = merge
    
    return value_table, merge_table

def unmerge(value_table, merge_table, indices):
    value = value_table[indices[0]][indices[1]]
    merged_sells = merge_table[indices[0]][indices[1]]
    if merged_sells == 0 or merged_sells == [indices]:
        return value_table, merge_table
    
    for merged_sell in merged_sells:
        value_table[merged_sell[0]][merged_sell[1]] = 0
        merge_table[merged_sell[0]][merged_sell[1]] = []
        
    value_table[indices[0]][indices[1]] = value
    merge_table[indices[0]][indices[1]] = [indices]
    
    return value_table, merge_table

def print_func(value_table, indices):
    if value_table[indices[0]][indices[1]] == 0:
        return "EMPTY"
    
    return value_table[indices[0]][indices[1]]