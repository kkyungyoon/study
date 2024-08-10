def solution(my_string, index_list):
    answer_list = []
    for i in index_list:
        answer_list.append(my_string[i])
    answer = ''.join(answer_list)
    return answer

    # return ''.join([my_string[idx] for idx in index_list])