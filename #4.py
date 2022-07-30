a = 2
b = 3

s = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
g = ' '
z = ' '
j=' '
k=' '
for i in s:
    if (i % a == 0 and not i % b == 0):
        z += str(s[i])+" "
    elif (not i % a == 0 and i % b == 0):
        g += str(s[i]) + " "
    elif (i % a == 0 and i % b == 0):
        j += str(s[i]) + " "
    elif (not i % a == 0 and not i % b == 0):
        k += str(s[i]) + " "

print(z,"-> total nonb:",len(z.strip().split(" ")))
print(g,"-> total nonb:",len(g.strip().split(" ")))
print(j,"-> total nonb:",len(j.strip().split(" ")))
print(k,"-> total nonb:",len(k.strip().split(" ")))