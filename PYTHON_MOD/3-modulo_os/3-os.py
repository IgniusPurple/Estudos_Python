import os


# 1 - Consultar funcionalidades do módulo OS
help('os')

# 2 - Retornar a pasta atual

print(os.getcwd())

# 3 - Listar arquivos e pastas
print(os.listdir())


# 4 - Apresentar a versão da SO
os.system('lsb_release -a')


# 5 - Configurações da máquina
os.system('lshw')


# 6 - Limpar a tela do terminal
os.system('clear')