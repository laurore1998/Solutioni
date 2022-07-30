import string
a=string.ascii_uppercase

b="<1N <7H <0T <3S >2J <6U <5Y >8D >5D >1A"
#print(b[0:][1+3])
b=b.split()
s=""
for i in range(len(b)):
    if b[i][0] == ">":
        s+=a[a.index(b[i][2]) + int(b[i][1])]
    else:
        s+=a[a.index(b[i][2]) - int(b[i][1])]

print(s)
