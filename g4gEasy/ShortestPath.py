import sys

n = int(sys.stdin.readline())

while n > 0 :
    arrStr = sys.stdin.readline().strip()
    arr = [int(e) for e in arrStr.split(" ")]

    def findPath(n, m):
        if n == 0 and m == 0:
            return 0;
        elif n == 0 or m == 0:
            return 1
        elif n == 1:
            return m + 1
        elif m == 1:
            return n + 1
        else:
            return findPath(n - 1, m) + findPath(n, m - 1)

    print(findPath(arr[0],arr[1]))
    n -=1