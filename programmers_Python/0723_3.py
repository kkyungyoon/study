def solution(n_str):
    for num in n_str:
        if num == '0':
            n_str = n_str.lstrip('0')
        else: break
    return n_str

    # 다른사람 풀이
    # return n_str.lstrip('0')