nome = str(input('Qual seu nome completo? ').strip())
primeiro = nome.split()
print(f'Nome completo em maiusculo: {nome.upper()}')
print(f'Nome completo em minusculo: {nome.lower()}')
print(f'Quantidade de letras sem espaços: {len(nome)}')
print(f'Quantidade de letras do primeiro nome: {len(primeiro[0])}')