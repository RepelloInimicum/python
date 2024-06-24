# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

número = int(input('Digite um valor qualquer: '))

for i in range(1, 11):
	print(f'{número:2} x {i:2} = {número * i:2}')