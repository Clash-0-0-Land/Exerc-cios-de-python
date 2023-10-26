n= int(input('Há quantos dias o carro foi alugado? '))
m= int(input('Quantos KM o carro andou? '))
r= n*60
km= m*0.15
rkm= r+km
print ('O total a ser pago é R${}.' .format(rkm))