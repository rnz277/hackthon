# Colocado em evidência o valor do salario minimo e a quantidades de horas trabalhadas.
hrtrabalhada = float(input('Digite o numero de horas trabalhadas: '))
salario = float(input('Digite o salario minimo: '))

# Quantidade de hora trabalhada e igual ao meio do salario minimo.
hrtrabalhadas = salario /2

# Horas trabalhadas vezes a metade do salario minimo.
slbruto = hrtrabalhada * hrtrabalhadas

# Valor do imposto do salario.
imposto = 3 /100

# O valor do imposto vezes o salario bruto.
imposto1 = slbruto * imposto

# O  a subtração do imposto no salario final.
iptl = slbruto - imposto1

# Conclusão.
print(f'o salario total a receber é: {iptl}')
