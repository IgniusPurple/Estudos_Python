import pprint

gameDict = {
    'Resident evil 4':{
        'yearLaunch': 2023,
        'classification': 9.8,
        'genre': ['ação', 'aventura']
        
    },
    'mario odyssey':{
        'yearLaunch': 2017,
        'classification': 10,
        'genre': ['3D', 'aventura']
    },
    'donkey kong country':{
        'yearLaunch': 1995,
        'classification': 9.5,
        'genre': ['plataforma', 'aventura']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gameDict)


# 1 - Buscar informação dentro de um Dicionário Aninhado
print(gameDict['mario odyssey']['genre'])

# 2 - Adicionar novo item
gameDict['mario odyssey']['players'] = 1
print(gameDict['mario odyssey'])

# 3 -  Excluir um dicinário
del gameDict['Resident evil 4']
pp.pprint(gameDict)