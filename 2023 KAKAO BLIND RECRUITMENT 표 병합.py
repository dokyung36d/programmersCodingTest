## merge table에서 만약 있으면 각 element는 tuple 형식

# 1, 13, 14, 15, 16, 19
import copy

def solution(commands):
    value_table = [[-1 for _ in range(50)] for _ in range(50)]
    merge_table = [[[(j, i)] for i in range(50)] for j in range(50)]
    
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

def update_by_location(value_table, merge_table, indices : tuple, value):
    prev_value = value_table[indices[0]][indices[1]]
    
    for merged_indices in merge_table[indices[0]][indices[1]]:
        value_table[merged_indices[0]][merged_indices[1]] = value
        
    return value_table, merge_table

def update_by_value(value_table, origin_value, change_value): ##Need Refactoring
    for i in range(50):
        for j in range(50):
            if value_table[i][j] == origin_value:
                value_table[i][j] = change_value
                
    return value_table

def merge(value_table, merge_table, indices_1, indices_2):
    if indices_2 in merge_table[indices_1[0]][indices_1[1]]:
        return value_table, merge_table
    
    if indices_1 in merge_table[indices_2[0]][indices_2[1]]:
        return value_table, merge_table
    assert (indices_1 in merge_table[indices_2[0]][indices_2[1]])
    
    if value_table[indices_1[0]][indices_1[1]] == -1 and value_table[indices_2[0]][indices_2[1]] == -1: ##태초의 상태
        merge_table[indices_1[0]][indices_1[1]].extend(merge_table[indices_2[0]][indices_2[1]])
        merged_list = list(set(merge_table[indices_1[0]][indices_1[1]]))
        
        for merged in merged_list:
            merge_table[merged[0]][merged[1]] = merged_list
            value_table[merged[0]][merged[1]] = -1

            
        return value_table, merge_table
    
    
    if value_table[indices_1[0]][indices_1[1]] == -1 and value_table[indices_2[0]][indices_2[1]] != -1:

        merge_table[indices_2[0]][indices_2[1]].extend(merge_table[indices_1[0]][indices_1[1]])
        merged_list = list(set(merge_table[indices_2[0]][indices_2[1]]))
        
        for merged in merged_list:
            value_table[merged[0]][merged[1]] = value_table[indices_2[0]][indices_2[1]]
            merge_table[merged[0]][merged[1]] = merged_list
            
        
        return value_table, merge_table
    
    
    if value_table[indices_1[0]][indices_1[1]] != -1:
        merge_table[indices_1[0]][indices_1[1]].extend(merge_table[indices_2[0]][indices_2[1]])
        merged_list = list(set(merge_table[indices_1[0]][indices_1[1]]))
        
        for merged in merged_list:
            value_table[merged[0]][merged[1]] = value_table[indices_1[0]][indices_1[1]]
            merge_table[merged[0]][merged[1]] = merged_list
            

        return value_table, merge_table
    
    else:
        return False
    
    

def unmerge(value_table, merge_table, indices):
    value = value_table[indices[0]][indices[1]]
    merged_sells = merge_table[indices[0]][indices[1]]
    
    if merged_sells == [indices]:
        return value_table, merge_table
    
    for merged_sell in merged_sells:
        value_table[merged_sell[0]][merged_sell[1]] = -1
        merge_table[merged_sell[0]][merged_sell[1]] = [merged_sell]
        
    value_table[indices[0]][indices[1]] = value
    merge_table[indices[0]][indices[1]] = [indices]
    
    return value_table, merge_table



def print_func(value_table, indices):
    if value_table[indices[0]][indices[1]] == -1:
        return "EMPTY"
    
    return value_table[indices[0]][indices[1]]