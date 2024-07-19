def solution(n, control):
    # for cond in control:
    #     if cond == 'w':
    #         n+=1
    #     elif cond == 's':
    #         n-=1
    #     elif cond == 'd':
    #         n+=10
    #     elif cond == 'a':
    #         n-=10
    # return n
    
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])