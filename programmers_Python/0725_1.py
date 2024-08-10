def solution(myString):
    del_list = ['a','b','c','d','e','f','g','h','i','j','k']
    for st in myString[:]:
        if st in del_list:
            myString = myString.replace(st, 'l')
        else:
            continue
    return myString

    # 다른 사람 풀이
    # return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))