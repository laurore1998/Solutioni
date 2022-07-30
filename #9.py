a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17,18,19,20]
o = []
d = 0
for el in a:
    if el % 2 == 0:
        o.append(el)
        d = sum(o)

print(d)
print(o)
