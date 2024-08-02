def solution(friends :list, gifts : list):
    friend_map = {}

    num_friends=0
    for friend in friends:
        friend_map[friend] = num_friends
        num_friends +=1

    gift_matrix = [[0 for _ in range(num_friends)] for _ in range(num_friends)]
    
    for gift in gifts:
        giver, reciever = gift.split()[0], gift.split()[1]
        giver_id, reciever_id = friend_map[giver], friend_map[reciever]

        gift_matrix[giver_id][reciever_id] += 1
    
    gift_index_list = get_gift_index(gift_matrix = gift_matrix)


    last_month_gift_list = [0 for _ in range(num_friends)]

    for i in range(num_friends):
        for j in range(i + 1, num_friends):
            result = decide_who_gets_gift(i, j, gift_matrix = gift_matrix,
                                          gift_index_list = gift_index_list)

            last_month_gift_list = apply_result_to_last_month_gift_list(i, j, result= result,
                                                                        last_month_gift_list = last_month_gift_list)
    answer = max(last_month_gift_list)
    return answer

def get_gift_index(gift_matrix):
    give_gifts_sum_list = []
    for i in range(len(gift_matrix)):
        give_gifts_sum_list.append(sum(gift_matrix[i]))

    recieve_gifts_sum_list = [0 for _ in range(len(gift_matrix))]
    for i in range(len(gift_matrix)):
        recieve_gifts_sum_list = [a + b for a, b in zip(recieve_gifts_sum_list, gift_matrix[i])]

    return [a - b for a, b in zip(give_gifts_sum_list, recieve_gifts_sum_list)]

def decide_who_gets_gift(index1, index2, gift_matrix, gift_index_list):
    ## returns who gets gift
    ## if index1 gets gift, return 1
    ## if index2 gets gift, return 2
    ## if no one gets gift, return 0

    ##First Comparison
    numIndex1GivesToIndex2 = gift_matrix[index1][index2]
    numIndex2GivesToIndex1 = gift_matrix[index2][index1]



    if (numIndex1GivesToIndex2 != 0 or numIndex2GivesToIndex1 != 0) and (numIndex1GivesToIndex2 > numIndex2GivesToIndex1):
        return 1
    if (numIndex1GivesToIndex2 != 0 or numIndex2GivesToIndex1 != 0) and (numIndex1GivesToIndex2 < numIndex2GivesToIndex1):
        return 2

    ## Second Comparison
    if gift_index_list[index1] > gift_index_list[index2]:
        return 1
    if gift_index_list[index1] < gift_index_list[index2]:
        return 2
    return 0

def apply_result_to_last_month_gift_list(index1, index2, result, last_month_gift_list):
    if result == 1:
        last_month_gift_list[index1] += 1

    elif result == 2:
        last_month_gift_list[index2] += 1

    return last_month_gift_list




if __name__ == "__main__":
    friends = ["a", "b", "c"]
    gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
    print(solution(friends, gifts))
