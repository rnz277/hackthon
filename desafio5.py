# Expõem o valor das variaveis.
salario = float(input('Digite o salario atual: '))
percentual = float(input('Digite a porcentagem de aumento: '))

# Valor da taxa percentual de aumento.
percentual1 = percentual /100

# Valor da taxa percentual com o salario.
salarionv = salario * percentual1

# Soma do valor da taxa com o salario atual.
salario2 = salarionv + salario

# Subtração do salario novo com o antigo para indentificar o valor de aumento. 
vlaumento = salario2 - salario

# Conclusão.
print(f'O salario atual é: {salario2}, e um aumento de: {vlaumento}.')