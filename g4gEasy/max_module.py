import sys

t = int(sys.stdin.readline())

for i in range(t):
    step = int(sys.stdin.readline().strip().split(" ")[1])
    arrStr = sys.stdin.readline().strip()
    arr = [int(i) for i in arrStr.split(" ")]

    arr.sort()

    ll = int(len(arr) / 2 - 1) if len(arr)%2 == 0 else int(len(arr) / 2)
    r_steps = 0;
    base_element = arr[ll]

    flag = False
    for e in arr:
        diff = e - base_element if e > base_element else base_element - e;
        if diff % step == 0:
            r_steps += diff / step
        else:
            flag = True
            break

    if flag:
        print(-1)
    else:
        print(int(r_steps))
