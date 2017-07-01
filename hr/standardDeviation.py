import math
import sys

N = sys.stdin.readline()
aList = [int(i) for i in sys.stdin.readline().split()]

mean = sum(aList)/float(N)

diff_lr = [ (e - mean)**2 for e in aList]

sd = math.sqrt(sum(diff_lr)/float(N))
print("%.2f" % sd)