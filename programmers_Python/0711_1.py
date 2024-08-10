# n = 3, 첫번째 자리가 정해졌을때 list의 개수 : 2*1 
# n = 4, 첫번째 자리가 정해졌을때 list의 개수 : 3*2*1 
# 즉, 첫번째 자리가 정해졌을 때, 뒤 숫자의 경우의 수 : (n-1)!

# n = 3, 첫번째 자리, 두번째 자리가 정해졌을 때 list의 개수 : 1
# n = 4, 첫번째 자리, 두번째 자리가 정해졌을 때 list의 개수 : 2*1
# 즉, 첫번째 자리, 두번째 자리가 정해졌을 때, 뒤 숫자의 경우의 수 : (n-2)!

import math

def solution(n, k):
    answer = []
    alist = [i for i in range(1,n+1)]
    while alist:
        fac = math.factorial(n-1)
        idx = (k-1) // fac #몫
        a = alist.pop(idx)
        answer.append(a)
        n -= 1
        k = k % fac
    return(answer)