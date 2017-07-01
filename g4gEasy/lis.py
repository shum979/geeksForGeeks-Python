import sys

cases = int(sys.stdin.readline())

for t in range(cases):
    psize = int(sys.stdin.readline())
    arrString = sys.stdin.readline().strip()
    arr = [int(i) for i in arrString.split(" ")]

    max_sq = 0
    curr_sq = 0
    size = len(arr)
    i = 0
    flag = True;
    while i < size:
        if i == size - 1 and arr[size - 1] < arr[0] and flag:
            curr_sq += 1
            # print(arr[size -1],arr[0])
            i = 0;
            flag = False
        if i < size - 1 and arr[i] < arr[i + 1]:
            # print(arr[i],arr[i+1])
            curr_sq += 1
        else:
            max_sq = curr_sq if curr_sq > max_sq else max_sq
            curr_sq = 0
            if not flag:
                break;
        i += 1
    print(max_sq + 1)
