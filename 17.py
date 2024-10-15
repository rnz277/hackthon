# Primeiro adicionamos a variavel de numero:
num = int(input('Digite um numero: '))

# Depois, armazenamos os valores pares numa lista:
par = [0,2,4,6,8,10,12,14,16,18,20,24,26,28,30,32,34,36,38,40,42,44,46,48,50]

# E por ultimo, usamos o if,else para confirmar se tal numero e par ou impar:
if num in par:
    print('É par!')
else:
    print('É impar!')