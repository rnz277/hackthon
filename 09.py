# Primeiro, adicionamos as variaveis dos catetos:
cat1 = float(input('Digite o valor de um cateto: '))
cat2 = float(input('Digite o valor de um cateto: '))

# Depois adicionamos a variavel da hipotenusa para multiplicar os catetos ao quadrado:
hipotenusa = cat1**2 * cat2**2

# Depois criamos outra variavel para o valor da hipotenusa estar em raiz:6
hp = hipotenusa**0.5
print(f'A hipotenusa desse triangulo é: {hp:.1f}')
