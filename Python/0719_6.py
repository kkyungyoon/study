def solution(num_list):
    answer1 = []
    answer2 = []
    for num in num_list:
        if num % 2 == 1:
            answer1.append(num)
        elif num % 2 == 0:
            answer2.append(num)
    ans1 = int(''.join(map(str, answer1)))
    ans2 = int(''.join(map(str, answer2)))
    return ans1 + ans2