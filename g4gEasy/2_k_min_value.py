#code
import string

d = dict.fromkeys(string.ascii_lowercase, 0)

s = "fxnsmkasmlerxxoxhfwviluzttqqotdwrsqfcsxrddicaxahewemjyleudukxzgqrzvvrtmvwvxzuxiyvnngna"
for x in s:
    d[x] = d[x]+1
k=21
for b in range(k):
    m = max(d, key=d.get)

    # print(d)
    # print(m)
    d[m] = d[m]-1
#print(len(s))
#print(sum(d.values()))
print(d)
sm=0
for a in d.keys():
    if d[a] > 0:
        sm=sm+d[a]*d[a]
print(sm)

