import sys

#problem statement
#http://practice.geeksforgeeks.org/problems/number-of-groups/0

def ncr(n, r):
    product = 1;
    deno = 1;
    for x in range(r):
        product *= (n - x)
        deno *= (x + 1)
    return int(product / deno)


def solution2(arr_str):
    # arr_str = "3 6 9 12"
    zeros = 0;
    ones = 0;
    twos = 0;

    for i in arr_str.split(" ") :
        if int(i) % 3 == 0 :
            zeros +=1
        elif int(i) % 3 == 1 :
            ones += 1
        else:
            twos +=1

    print(zeros,ones,twos)
    count = ncr(zeros,2) + ones*twos + ncr(ones,3) + ncr(zeros,3) + ncr(twos,3) + zeros*ones*twos;
    print(count)


cases = int(sys.stdin.readline())
for n in range(cases):
    size = int(sys.stdin.readline());
    arr_str = sys.stdin.readline().strip()
    solution2(arr_str)

# solution2("1 5 7 2 9 14")