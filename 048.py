s= 0
g= 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        g+=1
        s+=c
print ('A soma de {} valores é {}.' .format(s, g))