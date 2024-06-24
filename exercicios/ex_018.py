# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Ângulo: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'{'ÂNGULO':<10}{angulo:>05.2f}')
print(f'{'SENO':<10}{seno:0>5.2f}')
print(f'{'COSSENO':<10}{cosseno:0>5.2f}')
print(f'{'TANGENTE':<10}{tangente:0>5.2f}')