def solution(strArr):
    for idx, string in enumerate(strArr[:]):
        if idx % 2 == 1:
            strArr[idx] = string.upper() 
        else: 
            strArr[idx] = string.lower()
    return strArr  