# Primeiro, adicionamos a variavel de numero:
num = float(input('Digite um numero: '))

# Depois listamos os multiplos de 3:
multiplo_3 = [3,6,9,12,15,18,21,24,27,30,33,36,38,42,45]

# Por ultimo, usamos o if,else para confirmar se tal numero e multiplo de 3 ou nao:
if num in multiplo_3:
    print('É multiplo de 3!')
else:
    print('Não é multiplo de 3!')


