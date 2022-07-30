
a="127.0.0.0.1"

a=a.split(".")
chen_1=a[0]
e=0

for i in a:
    e *= int(chen_1[0])
    for s in i:
        e+=int(s)

print(e)