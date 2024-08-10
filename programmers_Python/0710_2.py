def solution(strings, n):
    answer = strings[:]
    answer.sort(reverse=False)
    answer.sort(reverse=False, key= lambda x: x[n])
    return answer