## Emotion의 크기가 작음 -> Emotion을 기준으로 dfs, bfs 진행해도 좋을 듯
## 총 경우의 수 : 4^7
## 1차 목표 : 가입자 늘리는 것 -> 일단 많이 구매 -> 할인율 높이기
## -> dfs로 진행하면 좋을 듯
## 일정 숫자 이상 이모티콘 안사면 바로 pruning
import copy
import sys
sys.setrecursionlimit(10**6)

def solution(users, emoticons):
    result = dfs(users, emoticons, [], 0)
    
    answer = [result[0], result[1]]
    return answer

def dfs(users, emoticons, discount_list : list, depth : int, max_num_new_member = 0, max_total_pay = 0): ##depth는 0에서부터 시작
    if depth == len(emoticons):
        result = get_result(users, emoticons, discount_list)
        
        if result[0] < max_num_new_member:
            pass
            # return (max_num_new_number, max_total_pay)
        
        elif result[0] == max_num_new_member and result[1] > max_total_pay:
            max_total_pay = result[1]
            
        elif result[0] > max_num_new_member:
            max_num_new_member = result[0]
            max_total_pay = result[1]
            
    discount_rate_list = [40, 30, 20, 10]
    
    for discount_rate in discount_rate_list:
        copied_discount_list = copy.deepcopy(discount_list)
        copied_discount_list.append(discount_rate)
        
        dfs_result = dfs(users, emoticons, copied_discount_list, depth + 1, max_num_new_member, max_total_pay)

        if dfs_result[0] < max_num_new_member:
            pass
            # return (max_num_new_number, max_total_pay)
        
        elif dfs_result[0] == max_num_new_member and dfs_result[1] > max_total_pay:
            max_total_pay = dfs_result[1]
            
        elif dfs_result[0] > max_num_new_member:
            max_num_new_member = dfs_result[0]
            max_total_pay = dfs_result[1]
            
    return (max_num_new_member, max_total_pay)

def get_result(users, emoticons, discount_list : list):
    num_new_number = 0
    total_pay = 0
    for i in range(len(users)):
        user_result = determine_buy_or_not(users[i], emoticons, discount_list)
        
        if user_result[0] == True: ##become new member of emoticon plus
            num_new_number += 1
        else: 
            total_pay += user_result[1]

    return (num_new_number, total_pay)

def determine_buy_or_not(user, emoticons, discount_list : list):
    become_new_member = False
    pay = 0

    for i in range(len(emoticons)):
        if discount_list[i] < user[0]:
            continue
            
        pay += (emoticons[i] * (discount_list[i] / 100))
        
    if pay >= user[1]:
        become_new_member = True
        pay = 0  ##이모티콘 플러스에 가입하므로 판매액은 0이 됨
        
    return (become_new_member, pay)