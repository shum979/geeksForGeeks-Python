import sys


def solution(arr_str):
    # arrStr = "3 6 9 12"
    arr = [int(i) for i in arr_str.split(" ")]
    cntr_2 = 0;
    cntr_3 = 0;

    while arr:
        first = arr.pop()
        newArr = list(arr)
        while newArr:
            second = newArr.pop()
            cntr_2 += 1 if ((first + second) % 3) == 0 else 0;
            for x in newArr:
                cntr_3 += 1 if ((first + second + x) % 3) == 0 else 0;

    print(cntr_2 + cntr_3)


cases = int(sys.stdin.readline())
for n in range(cases):
    size = int(sys.stdin.readline());
    arr_str = sys.stdin.readline().strip()
    solution(arr_str)
