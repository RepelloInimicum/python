# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
soma_catetos = cateto_adjacente ** 2 + cateto_oposto ** 2
hipotenusa = soma_catetos ** .5

print(f'{'ADJACENTE:':<12}{cateto_adjacente:>5.2f}')
print(f'{'OPOSTO:':<12}{cateto_oposto:>5.2f}')
print(f'{'HIPOTENUSA:':<12}{hipotenusa:>5.2f}')