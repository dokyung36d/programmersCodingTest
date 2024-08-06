## n이 큰 경우 bfs로 풀 때 시간이 너무 오래 걸릴 수 있음 -> dfs로 풀어야 할 듯
# import sys
# sys.setrecursionlimit(10**6)
import copy

def solution(coin, cards):
    n = len(cards)
    
    cards_in_hand = cards[:int(n / 3)]
    remain_cards = cards[int(n / 3):]
    
    result = get_results(cards_in_hand, remain_cards, remain_coin = coin, round = 1, n = n + 1)
    
    return result

def get_results(cards_in_hands : list, remain_cards : list, remain_coin : int, round : int, n : int):
    maximum_round_candidate_list = []

    if len(remain_cards) < 2: ## 더 이상 뽑을 카드가 없는 경우
        return round
    
    pick_cards = remain_cards[:2]
    remain_cards = remain_cards[2:]
    
    copied_cards_in_hands = copy.deepcopy(cards_in_hands)
    copied_remain_cards = copy.deepcopy(remain_cards)
    
    ## 두 장 모두 버리는 경우, 코인을 소모하지 않는 경우
    pick_result = pick_two_cards_to_n_plus_one(card_list = copied_cards_in_hands, target_number = n)

    if pick_result == False or len(copied_cards_in_hands) < 2:
        maximum_round_candidate_list.append(round)
    else:
        copied_cards_in_hands.pop(pick_result[1])
        copied_cards_in_hands.pop(pick_result[0])
        result = get_results(cards_in_hands = copied_cards_in_hands, remain_cards = remain_cards,
                          remain_coin = remain_coin, round = round + 1, n = n)
        maximum_round_candidate_list.append(result)
        
        
    copied_cards_in_hands = copy.deepcopy(cards_in_hands)
    copied_remain_cards = copy.deepcopy(remain_cards)
    
    ## 카드를 한 장만 수용하는 경우
    if remain_coin < 1:
        return max(maximum_round_candidate_list)
    
    copied_cards_in_hands.append(pick_cards[0])
    pick_result = pick_two_cards_to_n_plus_one(card_list = copied_cards_in_hands, target_number = n)
    if pick_result == False or len(copied_cards_in_hands) < 1:
        maximum_round_candidate_list.append(round)
        
    else:
        try:
            copied_cards_in_hands.pop(pick_result[1])
            copied_cards_in_hands.pop(pick_result[0])
            result = get_results(cards_in_hands = copied_cards_in_hands, remain_cards = remain_cards,
                              remain_coin = remain_coin - 1, round = round + 1, n = n)
            maximum_round_candidate_list.append(round)
        except Exception as e:
            return copied_cards_in_hands, pick_result
    
    
    copied_cards_in_hands[-1] = pick_cards[1]
    pick_result = pick_two_cards_to_n_plus_one(card_list = copied_cards_in_hands, target_number = n)
    if pick_result == False:
        maximum_round_candidate_list.append(round)
    else:
        try:
            copied_cards_in_hands.pop(pick_result[1])
            copied_cards_in_hands.pop(pick_result[0])
            result = get_results(cards_in_hands = copied_cards_in_hands, remain_cards = remain_cards,
                              remain_coin = remain_coin - 1, round = round + 1, n = n)
            maximum_round_candidate_list.append(round)
        except Exception as e:
            return copied_cards_in_hands, pick_result
    
    
    copied_cards_in_hands = copy.deepcopy(cards_in_hands)
    copied_remain_cards = copy.deepcopy(remain_cards)
    
    ## 카드를 2장 모두 수용하는 경우(= 코인을 2개 소모하는 경우)
    if remain_coin < 2:
        return max(maximum_round_candidate_list)
    
    copied_cards_in_hands.extend(pick_cards)
    pick_result = pick_two_cards_to_n_plus_one(card_list = copied_cards_in_hands, target_number = n)
    if pick_result == False:
        maximum_round_candidate_list.append(round)
    else:
        copied_cards_in_hands.pop(pick_result[1])
        copied_cards_in_hands.pop(pick_result[0])
        result = get_results(cards_in_hands = copied_cards_in_hands, remain_cards = remain_cards,
                          remain_coin = remain_coin - 2, round = round + 1, n = n)
        maximum_round_candidate_list.append(result)
        
    return max(maximum_round_candidate_list)
        
        
def pick_two_cards_to_n_plus_one(card_list : list, target_number : int):
    for i in range(len(card_list) - 1):
        target_remain = target_number - card_list[i]
        
        if target_remain in card_list[i + 1:]:
            return [i, card_list.index(target_remain)]
    
    return False