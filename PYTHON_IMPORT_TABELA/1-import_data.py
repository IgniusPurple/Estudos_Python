import pandas as pd

# 1 - Importando Dados
data = pd.read_excel('data/VendaCarros.xlsx')
print(data)

# 2 - Lista dos primeiros registros
print(data.head())

# 3 - Lista os últimos registros
print(data.tail())

# 4 - Contagem de valores por fabricante
print(data['Fabricante'].value_counts())