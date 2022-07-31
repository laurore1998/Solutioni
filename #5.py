a = "5 45 123 12"
a = a.split()
lisadd = []
y = 0
t=1

for y in range(len(a)):
    z=0
    for i in a[y]:
        z += int(i)
    lisadd.append(z)

for u in lisadd:
    t*=u
    

#print(lis)
print(t)





