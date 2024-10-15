# Indicado o valor da base e à altura.
altura =  float(input('Digite a altura deste triangulo: '))
base = float(input('Digite a base deste triângulo: '))

# Resolução do calculo da area,perimetro e diagonal.
area = base * altura
perimetro = 2 *(base + altura)
diagonal = base**2 + altura**2
dg = diagonal **0.5

# Conclusão.
print(f'A area de seu triagulo é: {area},seu perimetro: {perimetro},sua diagonal: {dg}.')