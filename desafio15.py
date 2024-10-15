# O valor da taxa de juros, prestação e dias de atraso
vlinicial = float(input('Digite o valor inicial da prestação: '))
dias = float(input('Digite a quantidade de dias de atraso: '))
taxa = float(input('Digite a porcetagem da taxa: '))

# Calculo do valor final da prestação.
prestação = vlinicial + (vlinicial * (taxa / 100)* dias)

# Conclusão
print(f'O valor final da prestação é: {prestação}.')