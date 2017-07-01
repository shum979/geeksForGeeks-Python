import sys

n = sys.stdin.readline()
nE = sys.stdin.readline().strip()
nF = sys.stdin.readline().strip()

elements = map(int,nE.split(" "))
frequency = map(int,nF.split(" "))

#print map(int,elements), map(int, frequency)

newList = []
lowerHalf = []
upperHalf = []

count = 0;
for e in elements:
    num = frequency[count];
    while num > 0:
        newList.append(e)
        num -= 1

    count += 1

lenght = len(newList)
newList.sort()

if lenght % 2 == 0:
    lowerHalf = newList[0:lenght / 2]
    upperHalf = newList[lenght / 2:lenght]
else:
    lowerHalf = newList[0:lenght / 2]
    upperHalf = newList[lenght / 2 + 1:lenght]


def getMedian(array):
    l = len(array)
    if l % 2 == 0:
        return float((array[l / 2 - 1] + array[l / 2]) / 2)
    else:
        return float(array[l / 2])


print getMedian(upperHalf) - getMedian(lowerHalf)
