def solution(players, callings):
    # for call in callings:
    #     for idx, player in enumerate(players[:]):
    #         if player == call:
    #             temp = players[idx-1] #poe
    #             players[idx-1] = players[idx] #kai
    #             players[idx] = temp #poe
    # return players
    # 시간초과문제
    
    # 해결
    now_dict = {player: i for i, player in enumerate(players)}
    for call in callings:
        idx = now_dict[call] # 3
        now_dict[call] -= 1 # 앞으로 한칸 땡김
        now_dict[players[idx-1]] += 1 # 앞선수 뒤로땡김
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players