a=input("text: ")
s="aeiouy "
r=""
l="*"
for i in a:
    if i in s:
        r+=i
    else:
        r+=l

print(r)



