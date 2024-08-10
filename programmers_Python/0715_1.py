def solution(num_list):
    multiple = 1
    for i in num_list:
        multiple = multiple*i 
    return sum(num_list) if len(num_list) >= 11 else multiple 