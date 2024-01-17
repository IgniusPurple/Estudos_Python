teams = {}
done = False

# Função para listar times
def print_teams():
    print("\nTimes Listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")
        
# Função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f'{i+1}. {player}')

while not done:
    # Opções do Programa
    print("\nO que você deseja Fazer?\n")
    print("1. Adcionar um time:")
    print("2. Remover um time")
    print("3. Listar um time:")
    print("4. Adicionar jogadores em um time:")
    print("5. Remover jogadores em um time:")
    print("6. Listar Jogadores em um time:")
    print("7. Sair\n")
    
    choice = input("> ")
    if choice == "1":
        team_name = input("Digite o nome do time:\n")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time Adicionado\n")
    
    elif choice == "2":
        print_teams()
        team_num = int(input("\nInforme o número do time que deseja remover:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            del teams[team_name]
            print("Time Removido\n")
        else:
            print("Número do time inválido.\n")
    
    elif choice == "3":
        print_teams()
   
    elif choice == "4":
        print_teams()
        team_num = int(input("\nInforme o número do time que deseja adicionar o jogador:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            player_name = input("Informe o nome do jogador:\n")
            teams[team_name]['players'].append(player_name)
            print('\nJogador adicionado no time')
        else:
            print("\nNúmero do time está inválido")
    
    elif choice == "5":
        print_teams()
        team_num = int(input("\nInforme o número do time que deseja excluir o jogador:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover:\n"))
            if player_num <= len(teams[team_name]['players']):
                 del teams[team_name]['players'][player_num - 1]
                 print('\nJogador removido do time.')
            else:
                print('\nNúmero do jogador inválido')
        else:
            print('\nNúmero do jogador inválido')
    
    elif choice == "6":
        print_teams()
        team_num = int(input("\nInforme o número do time que deseja listar os jogadores:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
        else:
            print("\nNúmero do time inválido")
    
    elif choice == "7":
        done = True 
    
    else:
        print("Opção inválida\n")