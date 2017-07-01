import sys

n = int(sys.stdin.readline())

def find_pair(p_sum, brr, ind, in_ind):
    xrr = list(brr)
    xrr.remove(brr[ind])
    xrr.remove(brr[in_ind])
    result = 0
    func_index = 0
    while func_index < len(xrr) and result == 0:
        fi_index = func_index + 1
        if xrr[func_index] > p_sum:
            func_index += 1
            continue
        while fi_index < len(xrr):
            if xrr[fi_index] > p_sum:
                fi_index += 1
                continue
            if xrr[func_index] + xrr[fi_index] == p_sum:
                # result = (xrr[func_index], xrr[fi_index])
                result =1
                break
            fi_index += 1
        func_index += 1
    return result



while n > 0 :
    n -=1
    m = int(sys.stdin.readline())
    arrStr = sys.stdin.readline().strip()
    arr = [int(i) for i in arrStr.split(" ")]
    index = 0
    pairList = list()
    final_result = 0
    while index < len(arr):
        inner_index = index + 1
        while inner_index < len(arr) and final_result == 0:
            p_sum = arr[index] + arr[inner_index]
            final_result = find_pair(p_sum, arr, index, inner_index)
            if final_result != 0:
                # print(arr[index], arr[inner_index], final_result)
                break
            inner_index += 1
        index += 1

    print(final_result)
