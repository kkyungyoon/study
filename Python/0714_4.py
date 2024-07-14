def solution(myString):
    my_list = list(myString)
    for idx, string in enumerate(my_list):
        if string == 'a':
            my_list[idx] = 'A'
        elif string == 'A':
            continue
        else:
            my_list[idx] = my_list[idx].lower()
    answer = ''.join(my_list)
    return answer