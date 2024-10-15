# O valor do salario como vairavel.
salario = float(input('Digite o salario: '))

# Valor do imposto.
imposto = 10 /100

# Somatoria da gratificação com o salario.
salario2 = salario + 50

# Indentificação do valor do imposto.
sltotal = salario2 * imposto 

# Subtração do salario com gratificação prlo o imposto.
sltotal2 = salario2 - sltotal

# Conclusão.
print(f'O salario após o imposto e de: {sltotal2}')