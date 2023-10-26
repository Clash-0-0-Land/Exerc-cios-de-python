m= 0
n= 0
for c in range(1, 6):
    p= float(input('Qual é o peso {}? ' .format(c)))
    if c == 1:
        m = p
        n = p
    else:
        if p > m:
            m= p
        if p < n:
            n= p
print('O maior peso é {} kg.' .format(m))
print('O menor peso é {} kg.' .format(n))