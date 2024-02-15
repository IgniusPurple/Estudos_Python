import random

# 1 - Selecione o valor aleatório de uma lista
list1 = [7,6,4,5,6,3,2,4,5,3,2,1]
print(random.choice(list1))

# 2 -  Gera um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

# 3 - Selecione um caractere aleatŕoio de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1,2))

s = "Olá Mundo"
print(random.sample(s,3))