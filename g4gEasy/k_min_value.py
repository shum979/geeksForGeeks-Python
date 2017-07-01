import operator,sys

input_str = "fxnsmkasmlerxxoxhfwviluzttqqotdwrsqfcsxrddicaxahewemjyleudukxzgqrzvvrtmvwvxzuxiyvnngna"
k = 21

freq_map = dict()

for e in input_str:
    cnt = freq_map.get(e,0)
    freq_map[e] = cnt+1

list_of_tpl = sorted(freq_map.iteritems(),key=operator.itemgetter(1),reverse=True)

for e in list_of_tpl :
    print e

p_sum = 0
for e in list_of_tpl :
    if k > 0 :
        k = k - e[1]
        diff = 0 if k >= 0 else k
        p_sum += diff**2
        print(e[1],diff)
    else:
        p_sum += e[1]**2
        print e[1]

print(p_sum)

