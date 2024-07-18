def solution(my_string, is_prefix):
    answer_list = []
    for i in range(1,len(my_string)+1):
        answer_list.append(my_string[:i])
    return 1 if is_prefix in answer_list else 0