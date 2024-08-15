##왼쪽을 비어두는 경우, 오른쪽을 비워두는 경우의 수를 각각 Count
##합칠 때에는 무슨 방향으로 합쳐지는 고려해야 함.
##분할 정복으로 해결

def solution(n, tops):
    answer = get_case_number(0, n, tops)
    return sum(answer) % 10007

def get_case_number(start_index, length, tops):
    if length == 1 and tops[start_index] == 1:
        return [1, 2, 0, 1]
    if length == 1 and tops[start_index] == 0:
        return [1, 1, 0, 1]
    
    left_length = length // 2
    
    right_length = length - length // 2
    right_start_index = start_index + left_length
    
    left_cases = get_case_number(start_index, left_length, tops)
    right_cases = get_case_number(right_start_index, right_length, tops)
    
    case_number = combine_two_tile(left_cases, right_cases)
    
    return case_number

def combine_two_tile(left_tile : list, right_tile : list):
    combine_list = [0 for _ in range(4)]
    
    combine_list[0] = left_tile[0] * (right_tile[0] + right_tile[1]) + left_tile[2] * right_tile[1]
    combine_list[1] = left_tile[1] * (right_tile[0] + right_tile[1]) + left_tile[3] * right_tile[1]
    combine_list[2] = left_tile[0] * (right_tile[2] + right_tile[3]) + left_tile[2] * right_tile[3]
    combine_list[3] = right_tile[3] * (left_tile[1] + left_tile[3]) + right_tile[2] * left_tile[1]
    
    return combine_list