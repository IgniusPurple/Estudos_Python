name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
gamePrice = float(input("Digite o preço do jogo: \n"))
planeIncluded = (input("Está incluso no serviço mensal: \n"))



print("###DADOS DO JOGO###")
print("===================")
# Alternativa 1
print("Nome do jogo: ", name)
print("Ano de lançamento do jogo: ", yearLaunch)
print("Preço do Jogo: ", gamePrice)
print("Está incluido no plano? ", planeIncluded)

#Alternativa 2
print("Nome do jogo:", name, "\nAno de lançamento:", yearLaunch, 
        "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço:", planeIncluded)

#Alternativa 3
print(f'Nome do jogo: {name} \nAno de Lançamento: {yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluso no plano: {planeIncluded}')
