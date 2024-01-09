gameFifa = {
    "name":"Fifa23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification":8.5,
    "genre":["esportes", "família"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))


# 1 - Recuperar um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get("classification"))

# 2 - Buscar apenas as chaves do dicinário
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicinário
print(gameFifa.values())

# 4 - Buscar itens do docionário com cave e valor
print(gameFifa.items())

# 5 - Adionoar itens no dicionário
gameFifa["players"] = 2 
print(gameFifa)

# 6 - Atualizar itens no dicionário
gameFifa.update({'players': 1})
print(gameFifa)

# 7 - Remover item no dicionário
gameFifa.pop("players")
print(gameFifa)
