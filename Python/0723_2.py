def solution(num_list):
    answer1 = 0
    answer2 = 0
    for i in range(1, len(num_list)+1, 2):
        answer1 += num_list[i-1]
    for i in range(2, len(num_list)+1, 2):
        answer2 += num_list[i-1]
    return max(answer1, answer2)

    # 다른 사람 풀이
    # return max(sum(num_list[::2]), sum(num_list[1::2]))