def solution(myString, pat):
    string_list = list(myString)
    for idx, string in enumerate(string_list):
        if string == 'A':
            string_list[idx] = 'B'
        else:
            string_list[idx] = 'A'
    answer = ''.join(string_list)
    return 1 if pat in answer else 0