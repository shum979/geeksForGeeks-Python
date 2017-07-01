# code
import math, sys
from time import gmtime, strftime

n = int(sys.stdin.readline())

while n > 0:
    x1, y1 = sys.stdin.readline().strip().split(" ")
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    x = int(x1)
    y = int(y1)


    def isPrime(x):
        dm = 3
        if x == 2:
            return True
        elif x % 2 != 0:
            y = (int)(math.sqrt(x)) + 1
            while dm < y:
                if x % dm == 0:
                    return False
                    break
                dm += 1
            return True
        else:
            return False


    def isDPrime(x, lst):
        if len(lst) == 0:
            return True
        for j in lst:
            if x % j == 0:
                return False
            else:
                return True


    arr = list()
    counts = dict()
    while x <= y:
        if isDPrime(x, arr) and isPrime(x):
            arr.append(x)
            s = str(x)
            l = len(s) - 1
            print x
            while l >= 0:
                cnt = counts.get(s[l], 0)
                newCnt = cnt + 1
                counts[s[l]] = newCnt
                l -= 1
        x = x + 6 if x % 2 == 0 else x + 7

    maxKey = '-1'
    maxValue = 0
    for key, value in counts.items():
        if value >= maxValue:
            maxValue = value
            maxKey = maxKey if int(maxKey) > int(key) else key

    print(maxKey)
    n -= 1
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
