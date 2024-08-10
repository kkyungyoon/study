def solution(arr):
    for idx, ar in enumerate(arr):
        if ar >= 50 and ar % 2 == 0:
            arr[idx] = ar / 2
        elif ar < 50 and ar % 2 == 1:
            arr[idx] = ar * 2
        else:
            continue
    return arr