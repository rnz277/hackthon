# Indentifica a unidade de medida pés para efetuar as conversões.
pes = float(input('Digite o valor em pés: '))

# Indentifica as unidades de medidas que serão convertidas.
polegadas = pes * 12
jarda = pes /3
milha = jarda / 1760

# Conclusão.
print(f'o resultado em polegadas é: {polegadas}')
print(f'o resultado em jardas é: {jarda}')
print(f'o resultado em milhas é: {milha}')