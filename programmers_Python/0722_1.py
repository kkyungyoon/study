def solution(str_list, ex):
    answer = [word for word in str_list if ex not in word]
    return ''.join(answer)