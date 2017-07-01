import math,sys

t = int(sys.stdin.readline())

for e in range(t) :
    n = int(sys.stdin.readline())
    def isPrime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True



    upper = n+1
    lower = n-1

    while True :
        if isPrime(n):
            print(n)
        if isPrime(lower) :
            print(lower)
            break
        lower -=1

        if isPrime(upper) :
            print(upper)
            break
        upper +=1