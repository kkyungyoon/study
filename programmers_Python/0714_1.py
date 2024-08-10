def solution(rny_string):
    for string in rny_string[:]:
        if string == 'm':
            rny_string = rny_string.replace('m', 'rn')
        else:
            continue
    return rny_string

def solution(rny_string):
    return rny_string.replace('m', 'rn') if 'm' in rny_string else rny_string