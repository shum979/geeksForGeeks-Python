import sys
numOfCases = int(sys.stdin.readline())

while numOfCases > 0 :
    N = int(sys.stdin.readline())
    arrStr = sys.stdin.readline().strip()
    arr = [int(e) for e in arrStr.split(" ")]

    count = 0
    top = N
    i = N-1

    while i>=0:
        if arr[i]==top:
            top -= 1
            count += 1
        i -= 1
    count = N - count
    print(count)
    numOfCases -= 1


