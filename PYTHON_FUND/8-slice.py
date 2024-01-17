gameName = "Red Dead Redeption 2"

gameDescription = """
Red Dead Redemption 2 (estilizado Red Dead Redemption II) é um jogo eletrônico de ação-aventura
desenvolvido e publicado pela Rockstar Games. É o terceiro título da série Red Dead e uma prequela 
de Red Dead Redemption, tendo sido lançado em outubro de 2018 para PlayStation 4 e Xbox One e em 
novembro de 2019 para Microsoft Windows e Google Stadia. A história se passa em 1899 em uma 
representação ficcional do oeste, meio-oeste e sul dos Estados Unidos e acompanha o fora da lei Arthur 
Morgan, que precisa lidar com o declínio do Velho Oeste e sobreviver à perseguição de forças 
governamentais, gangues rivais e outros adversários.
"""

# string[inicio:fim] - indice (index) começa na posição 0 | indice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:20])

# 3 - Busque toda string a partir da 3° posição
print(gameName[2:])


"""
string[inicio:fim:passo] - indice (index) começa na posição 0 | indice final -1
passo - determina o ineceremento. Por padrão esse número é o 1

"""

# 4 - Busque toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - busque toda a string nos indices impares
print(gameName[1::2])

# 6 - Inverter uma string
print(gameName[::-1 ])