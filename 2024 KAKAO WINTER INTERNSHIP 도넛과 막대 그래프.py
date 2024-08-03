##일단 정점을 찾고 해당 정점에서 나온 점들을 기반으로 찾아야 할 듯
##정점을 제외한 모든 node들은 나가는 vertex가 오직 하나임. -> 틀림

def solution(edges):
    center_point, vertex_map = find_center_point_and_get_vertex_map(edge_list = edges)
    answer = [center_point, 0, 0, 0]

    for near_node in vertex_map[center_point]:
        shape = determine_shape(center_point = center_point, starting_node = near_node, vertex_map = vertex_map)
        answer[shape] += 1

    return answer

def find_center_point_and_get_vertex_map(edge_list : list):
    center_point_candidate_set = set()
    center_point_not_candidate_set = set()
    vertex_map = {}

    for edge in edge_list:
        center_point_candidate_set.add(edge[0])
        center_point_not_candidate_set.add(edge[1])
        if edge[0] not in vertex_map:
            vertex_map[edge[0]] = [edge[1]]
        else:
            vertex_map[edge[0]].append(edge[1])

    single_center_point_candidate_list = list(center_point_candidate_set - center_point_not_candidate_set)
    ## assert len(single_center_point_set) == 1 -> 첫번째 test case에서는 해당되지 않음
    for single_center_point_candidate in single_center_point_candidate_list:
        if len(vertex_map[single_center_point_candidate]) == 1:
            continue
        single_center_point = single_center_point_candidate
        break


    return single_center_point, vertex_map ##returns element in the set that has only one element

def find_near_node_from_center_point(edge_list : list, center_point : int):
    near_node_from_center_point_list = []

    for edge in edge_list:
        if edge[0] != center_point:
            continue

        near_node_from_center_point_list.append(edge[1])

    return near_node_from_center_point_list

def determine_shape(center_point : int, starting_node : int, vertex_map : dict):
    ## returns 1 when "donut"
    ## returns 2 when "line"
    ## returns 3 when "eight"

    if starting_node not in vertex_map: 
        return 2

    next_node = vertex_map[starting_node]

    if len(next_node) >= 2:
        return 3
    if next_node[0] == starting_node:
        return 1

    while next_node[0] != starting_node:
        if len(next_node) >= 2:
            return 3

        if next_node[0] not in vertex_map:
            return 2 ##도넛이나 8모양은 계속해서 생김

        next_node = vertex_map[next_node[0]]

        if len(next_node) >= 2:
            return 3

    return 1
