def solution(num_list):
    prod_num = 1
    for num in num_list:
        prod_num = prod_num*num
    return int(prod_num < sum(num_list)**2)