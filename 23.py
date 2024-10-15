# Primeiro, adicionamos as variaveis de peso e altura:
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# Depois criamos uma variavel para calcular o grau de obesidade:
grau_obesidade = peso / altura 

# Por ultimo, usamos o If para saber se o grau de obesidade esta conforme com o que esta sendo dito:
if grau_obesidade <=18.5:
    print('Voce esta magro!')

elif grau_obesidade <=18.5 and 24.9:
    print('Voce esta saudavel!')

elif grau_obesidade >=25.0 and 29.9:
    print('Voce esta em sobrepeso!')

elif grau_obesidade >=30.0 and 34.9:
    print('Voce esta com Obesidade grau 1!')

elif grau_obesidade >=35.0 and 39.9:
    print('Voce esta com Obesidade grau 2!')
    
elif grau_obesidade >=40.0:
    print('Voce esta com Obesidade grau 3!')