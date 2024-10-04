##알파벳 순서 상 d, i, r, u
## dfs 방법론으로

import sys
sys.setrecursionlimit(10**7)

def solution(n, m, x, y, r, c, k):
    start_point = (x, y)
    end_point = (r, c)
    distance = calculate_distance(start_point, end_point)
    
    remain_distance = k - distance
    if remain_distance % 2 == 1 or k < remain_distance:
        return "impossible"
    
    ## move 파트
    
    answer = dfs(start_point, end_point, k, n, m, "")
    return answer

def calculate_distance(start, end):
    distance = 0
    
    distance += abs(start[0] - end[0])
    distance += abs(start[1] - end[1])
    
    return distance

def calc_possible(cur_position, dest, remain_move):
    distance = calculate_distance(cur_position, dest)
    
    if (remain_move - distance) % 2 == 1:
        return False
    return True

def check_move_available(cur_pos, direction, n, m, dest, remain_move):
    move_dict = {"d" : (1, 0), "l" : (0, -1), "r" : (0, 1), "u" : (-1, 0)}
    
    moved_row = cur_pos[0] + move_dict[direction][0]
    moved_col = cur_pos[1] + move_dict[direction][1]
    
    if moved_row > n or moved_col > m or moved_row < 1 or moved_col < 1:
        return False
    
    if not calc_possible((moved_row, moved_col), dest, remain_move - 1):
        return False
    
    return (moved_row, moved_col)
    
def dfs(cur_position, dest, remain_move, n , m, answer : str): ##도착하고 낭비하는 case 고려해야 할 듯
    if calculate_distance(cur_position, dest) == remain_move:
        answer = find_fastest(cur_position, dest, answer)
        return answer ##여기서 이제 알파벳 순서대로 경로 설정, dfs는 더 이상 하지 않아도 됨
    
    
    move_list = ["d", "l", "r", "u"]
    
    for i in range(4):
        move_available = check_move_available(cur_position, move_list[i], n, m, dest, remain_move)

        if not move_available:
            continue
            
        return dfs(move_available, dest, remain_move - 1, n, m, answer + move_list[i])
    
    return "impossible"

def find_fastest(cur_pos, dest, answer : str): ##After using dfs
    if cur_pos == dest:
        return answer
    
    row_delta = dest[0] - cur_pos[0]
    col_delta = dest[1] - cur_pos[1]
    
    if row_delta > 0: ## d
        answer += "d" * row_delta
        
        if col_delta > 0:
            answer += "r" * col_delta
        else:
            answer += "l" * abs(col_delta)
            
            
    elif col_delta < 0: ## l
        answer += "l" * abs(col_delta)
        
        if row_delta > 0:
            answer += "d" * row_delta
        else:
            answer += "u" * abs(row_delta)
            
            
    elif col_delta > 0: ## r
        answer += "r" * col_delta
        
        if row_delta > 0:
            answer += "d" * row_delta
        else:
            answer += "u" * abs(row_delta)
            
            
    elif row_delta < 0: ## d
        answer += "d" * abs(row_delta)
        
        if col_delta > 0:
            answer += "r" * col_delta
        else:
            answer += "l" * abs(col_delta)
            
    return answer
            