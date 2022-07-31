
lst = [13, 4, 20, 15, 6, 29, 20]

sup=lst[0]
for i in lst:
    if sup < i:
        sup = i


print("superior: ",sup)

inf=lst[0]
for i in lst:
    if inf > i:
        inf = i


print("inferior: ",inf)
