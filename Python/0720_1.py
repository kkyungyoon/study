def solution(a, b):
    alist = [str(a), str(b)]
    blist = [str(b), str(a)]
    return max(int(''.join(alist)), int(''.join(blist)))

    # return int(max(f"{a}{b}", f"{b}{a}"))