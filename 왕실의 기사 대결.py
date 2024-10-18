##체스판의 크기가 그렇게 크지 않으므로 전체 탐색으로 해도 괜찮을 듯

L, N ,Q = map(int, input().split())

map_matrix = []
fighter_info_list = []
command_list = []

for _ in range(L):
    map_matrix.append(list(map(int, input().split())))

for _ in range(N):
    fighter_info_list.append(list(map(int, input().split())))

for _ in range(Q):
    command_list.append(list(map(int, input().split())))


def check_move_available(edge, height, width):
    pass

def change_fighter_position():
    global map_matrix
    pass