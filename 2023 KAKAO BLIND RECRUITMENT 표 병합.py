## merge table에서 만약 있으면 각 element는 tuple 형식

import copy

def solution(commands):
    for command in commands:
        result = process_instruction(command)
        
        return result
    answer = []
    return answer

def process_instruction(command):
    command_tuple = command.split(" ")
    
    if command_tuple[0] == "UPDATE" and len(command_tuple) == 4:
        pass
    
    if command_tuple[0] == "UPDATE" and len(command_tuple) == 3:
        pass
    
    if command_tuple[0] == "MERGE":
        pass
    
    if command_tuple[0] == "UNMERGE":
        pass
    
    if command_tuple[0] == "PRINT":
        pass
    
    return command_tuple

def update_by_location(value_table, merge_table, indices : tuple, value):
    value_table[indices[0]][indices[1]] = value
    
    return table

def update_by_value(value_table, origin_value, change_value): ##Need Refactoring
    for i in range(50):
        for j in range(50):
            if value_table[i][j] == origin_value:
                value_table[i][j] = change_value
                
    return table

def merge(value_table, merge_table, indices_1, indices_2):
    merge = merge_table[indices_1[0]][indices_1[1]]
    
    if merge_table[indices_2[0]][indices_2[1]] == [indices_2]: ##오직 혼자 구성되고, merge 하지 않은 상태
        merge_table.append(indices_2)
        value_table[indices_2[0]][indices_2[1]] = value_table[indices_1[0]][indices_1[1]]
        
        merge_table[indices_1[0]][indices_1[1]] = merge_table
        merge_table[indices_2[0]][indices_2[1]] = merge_table
        
        return merge_table
    
    merge.extend(merge_table[indices_2[0]][indices_2[1]])
    
    value_table[indices_2[0]][indices_2[1]] = value_table[indices_1[0]][indices_1[1]]
    merge_table[indices_1[0]][indices_1[1]] = merge
    merge_table[indices_2[0]][indices_2[1]] = merge
    
    return value_table, merge_table

def unmerge(indices, value_table, merge_table, initial_table):
    merged_sells = value_table[indices[0]][indices[1]]
    
    for merged_sell in merged_sells:
        value_table[merged_sell[0]][merged_sell[1]] = initial_table[merged_sell[0]][merged_sell[1]]
        merge_table[merged_sell[0]][merged_sell[1]] = [merged_sell]
        
    return value_table, merge_table