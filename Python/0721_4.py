def solution(arr, k):
    if k%2:
        return [a*k for a in arr]
    return [a+k for a in arr]

    # return [i*k if k%2!=0 else i+k for i in arr]