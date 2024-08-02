def solution(friends :list, gifts : list):
    friend_map = {}

    i=0
    for friend in friends:
        friend_map[friend] = i
        i +=1

    gift_matrix = [[0 for _ in range(i)] for _ in range(i)]
    
    for gift in gifts:
        giver, reciever = gift.split()[0], gift.split()[1]
        giver_id, reciever_id = friend_map[giver], friend_map[reciever]

        gift_matrix[giver_id][reciever_id] += 1
    
    gift_index_list = get_gift_index(gift_matrix = gift_index_list)


    answer = 0
    return answer

def get_gift_index(gift_matrix):
    give_gifts_sum_list = []
    for i in range(len(gift_matrix)):
        give_gifts_sum_list.append(sum(gift_matrix[i]))

    recieve_gifts_sum_list = [0 for _ in range(len(gift_matrix))]
    for i in range(len(gift_matrix)):
        recieve_gifts_sum_list = [a + b for a, b in zip(recieve_gifts_sum_list, gift_matrix[i])]

    return [a - b for a, b in zip(give_gifts_sum_list, recieve_gifts_sum_list)]
