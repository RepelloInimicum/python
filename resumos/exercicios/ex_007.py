# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite asegunda nota: '))
media = (nota_um + nota_dois) / 2

print(f'{'Primeira nota:':<15}{nota_um:>10}\n{'Segunda nota:':<15}{nota_dois:>10}\n{'Média: ':<15}\033[1;{31 if media < 5 else 32 if media > 6.9 else 33}m{media:>10.1f}\033[m')