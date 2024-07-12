def solution(name, yearning, photo):
    # name_list = [i for i in name]
    # yearning_list = [j for j in yearning]
    # name_tuple = tuple(name_list) # dict키값으로 쓰고자 튜플변환
    
    # dict 생성
    # dict={}
    # for i in range(len(name_list)):
    #     dict[name_list[i]] = yearning_list[i]

    # dict 생성 (zip으로 한번에 해결)
    dictionary = dict(zip(name,yearning))

    answer = []
    for pho in photo:
        sum = 0
        for person in pho:
            if person in name_list:
                sum += dict[person]
            else:
                continue
        answer.append(sum)
    return answer