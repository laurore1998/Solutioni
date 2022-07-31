import numpy

lst = [13, 4, 20, 15, 6, 24, 20]
sup=0
for i in range(len(lst)):
    if lst[0]>lst[i]:
        sup=lst[0]
    else:
        sup=lst[i]

print(sup)

