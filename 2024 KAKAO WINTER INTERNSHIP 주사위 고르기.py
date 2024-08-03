##tree문제에서 가지치기 n이 크지 않은 숫자여서 크게 문제 없을 듯
## 평균 취해서 하는 것은 반례 존재

## k번째 층에서는 k번째 주사위의 포함 여부를 결정
## 각 주사위를 선택했을 때의 경우의 수는 dp처럼 결과를 저장, dict 형태로

def solution(dice):
    answer = []
    return answer

def get_dict_after_accept_new_dice(previous_dict : dict, new_dice : list):
    for number in new_dice:
        new_dict = {}
        
        new_dict = get_dict_after_accept_new_number(previous_dict = previous_dict, new_number = number)
            
def get_dict_after_accept_new_number(previous_dict, new_number):
    pass