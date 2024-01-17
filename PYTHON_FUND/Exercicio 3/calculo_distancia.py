"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.

"""

distance = float(input("Qual a distância você deseja percorrer em quilômetros:\n\n"))

if distance <= 200:
    ticket = 0.50 * distance
else:
    ticket = 0.35 * distance

print(f'\nO valor da sua passagem foi de: R$ {ticket:.2f}')