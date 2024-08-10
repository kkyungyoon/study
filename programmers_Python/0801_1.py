def solution(a, b, c):
    if a != b and a != c and b != c:
        return a+b+c
    elif a == b and b == c:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        return (a+b+c)*(a**2+b**2+c**2)
    
    # 다른 사람 풀이
    # check=len(set([a,b,c]))
    # if check==1:
    #     return 3*a*3*(a**2)*3*(a**3)
    # elif check==2:
    #     return (a+b+c)*(a**2+b**2+c**2)
    # else:
    #     return (a+b+c)