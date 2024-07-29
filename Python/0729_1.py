def solution(strArr):
    answer = []
    for st in strArr[:]:
        if 'ad' not in st:
            answer.append(st)
        else:
            continue
    return answer
    # 다른 사람 풀이
    # return [word for word in strArr if 'ad' not in word]