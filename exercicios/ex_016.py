# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

numero = float(input('Digite um valor: '))
parte_inteira = numero // 1 # ou int(numero)
parte_decimal = numero % 1  # ou numero - parte_inteira

# Formatação
print(f'{'Número':<10}{numero:>10.5g}')
print(f'{'Inteiro':<10}{parte_inteira:>10.05g}')
print(f'{'Decimais':<10}{parte_decimal:>10.5g}')
# .5g é para mostrar 5 casas decimais significativas. Ou seja, 5 casas decimais que não são zeros