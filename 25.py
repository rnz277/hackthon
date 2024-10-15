# Primeiro, adicionamos uma variavel para letra:
letra = input('Digite uma letra: ')

# Depois armazenamos as vogais em uma lista:
vogal = ['a', 'e', 'i', 'o', 'u']

# Por ultimo, usamos o if, else para saber se a letra e vogal ou consoante:
if letra in vogal:
    print('É uma vogal.')
else:
    print('É uma consoante!')