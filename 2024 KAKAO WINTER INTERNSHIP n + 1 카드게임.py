## n이 큰 경우 bfs로 풀 때 시간이 너무 오래 걸릴 수 있음 -> dfs로 풀어야 할 듯
## 아이디어 : n이 커질 경우 처음에도 여러가지 경우의 수가 생길 수 있음, n + 1이 되는 짝이 여러 개 생길 수 있음
## 그럴 경우 한 노드 씩 천천히 가는 것 보다는 한꺼번에 여러 round를 처리하면 빠르게 처리 가능할 듯
# import sys
# sys.setrecursionlimit(10**6)
import itertools
import copy

def solution(coin, cards):
    n = len(cards)
    
    cards_in_hand = cards[:int(n / 3)]
    remain_cards = cards[int(n / 3) + 2:]
    
    result = get_results(cards_in_hand, remain_cards, pick_candidate_card_list = cards[int(n / 3):int(n / 3) + 2], remain_coin = coin, round = 1, n = n + 1)
    
    return result

max_record = 0

def get_results(cards_in_hands : list, remain_cards : list, pick_candidate_card_list : list, remain_coin : int, round : int, n : int):
    if len(remain_cards) < 2:
        return round
    
    
    result_in_hand_cards = pick_two_cards_to_n_plus_one(card_list = cards_in_hands, target_number = n)
    
    if result_in_hand_cards: ##손에 있는 카드로만으로도 n + 1이 가능한 경우
        del cards_in_hands[result_in_hand_cards[1]]
        del cards_in_hands[result_in_hand_cards[0]]
        
        pick_candidate_card_list.extend(remain_cards[:2])
        remain_cards = remain_cards[2:]
        
        return get_results(cards_in_hands, remain_cards, pick_candidate_card_list, remain_coin, round + 1, n)
    
    
    if remain_coin < 1: ##카드를 더 이상 후보에서 뽑을 수 없는 경우
        return round
    
    
    result_pair_in_hand_and_candidate = pick_pair_from_two_list(cards_in_hands, pick_candidate_card_list, target_number = n)
    
    if result_pair_in_hand_and_candidate:
        del cards_in_hands[result_pair_in_hand_and_candidate[0]]
        del pick_candidate_card_list[result_pair_in_hand_and_candidate[1]]
        
        pick_candidate_card_list.extend(remain_cards[:2])
        remain_cards = remain_cards[2:]
        
        return get_results(cards_in_hands, remain_cards, pick_candidate_card_list, remain_coin - 1, round + 1, n)
    
    if remain_coin < 2: ##후보에서 pair를 만들 수 없는 경우
        return round
    
    
    result_pair_in_candidate_list = pick_two_cards_to_n_plus_one(pick_candidate_card_list, target_number = n)
    
    if result_pair_in_candidate_list:
        del pick_candidate_card_list[result_pair_in_candidate_list[1]]
        del pick_candidate_card_list[result_pair_in_candidate_list[0]]
    
        pick_candidate_card_list.extend(remain_cards[:2])
        remain_cards = remain_cards[2:]
        
        return get_results(cards_in_hands, remain_cards, pick_candidate_card_list, remain_coin - 2, round + 1, n)
    
    return round ##모든 경우에서 pair를 찾지 못한 경우
        
        
def pick_two_cards_to_n_plus_one(card_list : list, target_number : int):
    for i in range(len(card_list) - 1):
        target_remain = target_number - card_list[i]
        
        if target_remain in card_list[i + 1:]:
            return [i, card_list.index(target_remain)]
    
    return False

def pick_pair_from_two_list(list1 : list, list2 : list, target_number : int):
    for pair in list(itertools.product(list1, list2)):
        if pair[0] + pair[1] == target_number:
            return [list1.index(pair[0]), list2.index(pair[1])]
    
    return False