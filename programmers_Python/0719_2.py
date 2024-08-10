def solution(my_strings, parts):
    answer_list = []
    for idx, word in enumerate(my_strings):
        answer_list.append(word[parts[idx][0]:parts[idx][1]+1])
    answer = ''.join(answer_list)
    return answer