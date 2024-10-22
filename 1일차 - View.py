def solution(building_info_list):
    total = 0

    for i in range(len(building_info_list)):
        ##Check Left
        if i == 0:
            total += check(building_info_list, i, [1, 2])

        elif i == 1:
            total += check(building_info_list, i, [-1, 1, 2])


        ##Check Right

        elif i == len(building_info_list) - 2:
            total += check(building_info_list, i, [-2, -1, 1])


        elif i == len(building_info_list) - 1:
            total += check(building_info_list, i, [-2, -1])


        else:
            total += check(building_info_list, i, [-2, -1, 1, 2])

    
    return total
        ##Normal Case


def check(building_info_list, curr_index, index_offset_range):
    curr_tall = building_info_list[curr_index]

    offset_tallest = building_info_list[curr_index + index_offset_range[0]]

    for i in range(1, len(index_offset_range)):
        if index_offset_range[i] == 0:
            continue
        offset_tall = building_info_list[curr_index + index_offset_range[i]]

        if offset_tall > offset_tallest:
            offset_tallest = offset_tall

    

    return max(0, curr_tall - offset_tallest)


for _ in range(10):
    N = int(input())

    info_list = list(map(int, input().split()))

    answer = solution(info_list)

    print(f"#{_ + 1} {answer}")