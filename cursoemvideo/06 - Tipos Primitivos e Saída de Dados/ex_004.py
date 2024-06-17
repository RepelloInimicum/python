# Exercício Python #004 - Dissecando uma Variável
# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


algo = input('Digite algo e veja algumas informações... ')
print(f'Você digitou "{algo}"')

# Como o tipo de dado de um input sempre é uma string, vamos avaliar antes se eventualmente um número for digitado.
try:
    # Tentamos converter a string para float. Se for possível significa implicitamente que a string é numérica, porém essa instrução não atualiza o dado. Serve apenas para a verificação e o dado continua sendo uma string.
    float(algo)

    # Verifica se a string original contém um ponto
    if '.' in algo:
        algo = float(algo)
    else:
        algo = int(algo)
except ValueError:
        print(f'Está em maiúsculas: {'Sim' if algo.isupper() else 'Não'}')
        print(f'Está em minúsculas: {'Sim' if algo.lower() else 'Não'}')
        print(f'É alfanumérico: {'Sim' if algo.isalnum() else 'Não'}')

print(f'O tipo de dado é {type(algo).__name__}')