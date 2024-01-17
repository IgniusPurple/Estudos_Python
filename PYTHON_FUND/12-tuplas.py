gamesTuple = ("Fifa 23", "Red Dead 2", "Star Wars", 
              "Mario Odyssey", "The Legend of Zelda")

print(gamesTuple)
print(type(gamesTuple))

# Não possibilita adicionar valors na Tupla
# Não possibilita remover valors na Tupla
# Não possibilita ordenar valors na Tupla


# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o utlimo item da lista
print(gamesTuple[-1])

# 3 - Buscar itens até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar itens de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item pela tupla pelo índice
print(gamesTuple.index("Red Dead 2"))