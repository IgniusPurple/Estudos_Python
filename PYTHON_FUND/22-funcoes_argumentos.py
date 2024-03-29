# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def fullName(fName, lName):
    print(f"Nome Completo:{fName} {lName}")

fullName('Matheus', 'Cavalcante')

# 2 - Crie uma função que some dois números via parâmetros
def sum(a,b):
    return a + b

print(sum(6,8))

# 3 - Argumentos default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
    
address()
address("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo:\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo:\n"))
        sum += note
    print(f'Média de avaliação do jogo {game_name} é : {sum/qtdRating:.2f}')

rating = int(input('Digite quantas avaliações deseja fazer no jogo:\n'))
rating_game(rating)
