n= input ('Digite uma frase: ')
g= n.upper()
p= g.count('A')
q= g.find('A')
t= g.rfind('A')

print ('Há {} A(s) na frase "{}".' .format(p,n))
print ('O primeiro "A" aparece na {}º posição de caracteres.' .format(q))
print ('O último "A" aparece na {}º posição de caracteres.' .format(t))