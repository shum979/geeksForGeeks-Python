import sys

cases = int(sys.stdin.readline())
for n in range(cases) :
    arrString = sys.stdin.readline().strip();
    arr = [int(i) for i in arrString.split(" ")]

    total = arr[0]
    initial = arr[1]
    steps = arr[2]

    nextMove = initial+steps
    counter = 1

    while nextMove != initial :
        nextMove = nextMove+steps if nextMove+steps < total else nextMove+steps -total
        counter +=1

    print(counter)
