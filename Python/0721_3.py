def solution(arr, delete_list):
    for num in arr[:]:
        if num in delete_list:
            arr.remove(num)
    return arr

    # return [i for i in arr if i not in delete_list]