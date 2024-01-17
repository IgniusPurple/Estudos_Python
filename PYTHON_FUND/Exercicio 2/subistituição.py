"""
Escreva um programa Python para obter uma string de uma determinada 
string em que todas as ocorrências de seu primeiro caractere 
foram alteradas para '$', exceto o próprio primeiro caractere

Ex:

fifa 23 → fi#a 23

restart→ resta#t
"""

name = input("Digite o nome do jogo: \n")

char = name[0].lower()
new_name = name.replace(char, "$")
new_name = char + new_name[1:]
print(new_name)
