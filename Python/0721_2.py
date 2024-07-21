def solution(myString):
    input_list = myString.split('x')
    return [len(word) for word in input_list]