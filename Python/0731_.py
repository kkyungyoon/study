def solution(arr, intervals):
    answer = []
    # for (a, b) in intervals:
    #     for k in arr[a:b+1]:
    #         answer.append(k)
    for a,b in intervals: answer+=arr[a:b+1]
    return answer