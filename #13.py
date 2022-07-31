lst = [0, 1, 2, 3, 4]
newl1 = []
newl2 = []
newl3 =[]

for i in range(len(lst)):
    if i == 0:
        newl1 = lst[::-1]
        # newl2 = newl1[0::]
    elif i == 1:
        newl2 = lst
        newl2.pop(0)
        newl2.insert(4, 0)
    elif i == 2:
        newl3 +=lst
        newl3.pop(4)
        newl3.pop(3)
        newl3=newl3[::-1]
        plist=[4,0]
        for l in reversed(plist):
            newl3.insert(3,l)


print(lst, "--> ", newl1)
print(newl1, "--> ", newl2)
print(newl2, "--> ", newl3)
