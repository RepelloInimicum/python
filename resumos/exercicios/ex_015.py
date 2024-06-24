# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


while True:
    try:
        km_percorrido = float(input('Km percorrido: '))  # Solicita e converte a entrada para float
        dias = int(input('Dias de aluguel: '))  # Solicita e converte a entrada para int

        valor_km = km_percorrido * 0.15  # Calcula o custo baseado nos km percorridos
        aluguel = dias * 60  # Calcula o custo baseado nos dias de aluguel
        total = valor_km + aluguel

        # Print formatado para mostrar os resultados
        print(f"{'KM Percorrido:':<20}{km_percorrido:^8.2f}Km\n"
              f"{'Valor KM:':<20}R${valor_km:>8.2f}\n"
              f"{'Dias aluguel:':<15}{dias:>8} dias\n"
              f"{'Valor aluguel:':<20}R${aluguel:>8.2f}\n"
              f"{'Total a pagar:':<20}R${total:>8.2f}")
        break  # Sai do loop se tudo correr bem
    except ValueError:
        print('Valor inválido! Tente novamente.')  # Mensagem de erro em caso de entrada inválida