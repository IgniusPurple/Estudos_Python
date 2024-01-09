gamesList = ["Resident Evil 4", "Star Wars Jedi Survivor",
             "The Legend of Zelda", "Red Dead Redemption 2",
             "Rainbow Six Siege"
             ]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recuperar um item da lista pelo índice
print(gamesList.index("Rainbow Six Siege"))

# 3 - Adicionar item ao final da lista
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordenar a lista
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para a outra
gamesReset = gamesList.copy()
gamesReset.remove("The Legend of Zelda")
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)