import pandas as pd
def solution(friends, gifts):
    name_list = {name: i for i, name in enumerate(friends)}
    check = {name: 0 for name in friends}
    df = pd.DataFrame(check, check)

    for gift in gifts:
        A, B = gift.split()
        df.iloc[name_list[A],name_list[B]] += 1
    print(df)

    give_list = []
    for row in range(len(friends)):
        give_list.append(df.iloc[row,:].sum())

    take_list = []
    for col in range(len(friends)):
        take_list.append(df.iloc[:,col].sum())

    index_list = []
    for idx in range(len(give_list)):
        index_list.append(give_list[idx] - take_list[idx])
    print(index_list)

    import numpy as np
    answer = np.zeros(len(friends))

    for row in range(len(friends)):
        for col in range(len(friends)):
            print(row, col)
            if df.iloc[row, col] > df.iloc[col, row]:
                print('*',row, col)
                answer[row] += 1
                print(answer)
                df.iloc[row, col] = 'n' 
                df.iloc[col, row] = 'n'
            elif df.iloc[row, col] < df.iloc[col, row]:
                print('**',row, col)
                answer[col] += 1
                print(answer)
                df.iloc[row, col] = 'n' 
                df.iloc[col, row] = 'n'
            elif df.iloc[row, col] != 'n' and df.iloc[col, row] != 'n':
                print('***',row, col)
                if index_list[row] > index_list[col]:
                    print(index_list[row])
                    print(index_list[col])
                    answer[row] += 1
                    df.iloc[row, col] = 'n' 
                    df.iloc[col, row] = 'n'
                elif index_list[row] < index_list[col]:
                    answer[col] += 1
                    df.iloc[row, col] = 'n' 
                    df.iloc[col, row] = 'n'
                else:
                    continue
    return (int(answer.max()))