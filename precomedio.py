#Preço médio notas escola

print ('Vamos calcular a média das suas notas!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#Maneiras simplificada de escrever o mesmo código

print ('Vamos calcular a média das suas notas!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')


    
