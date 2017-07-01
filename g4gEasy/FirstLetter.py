import sys

N = int(sys.stdin.readline())

while N > 0:
    N -= 1
    word = sys.stdin.readline().strip()
    p = ""
    for e in word.split(" "):
        if len(e) > 0:
            p += e[0]

    print( p)