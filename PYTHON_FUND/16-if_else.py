name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
classification = float(input("Digite a nota de classificação do jogo:\n"))


if classification > 8.0 and yearLaunch > 2015:
    print(f"""\nO jogo {name} possui uma nota de classificação de: {classification}. 
Sendo uma Boa recomendação. Além de ser lançado no ano de {yearLaunch}""")
    
else:
    print(f"""\nO jogo {name} possui uma nota de classificação de: {classification}. 
Sendo uma recomendação ruim. Além de ser lançado no ano de {yearLaunch}""")