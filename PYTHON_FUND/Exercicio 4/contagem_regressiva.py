"""
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”. 

"""

import winsound

x = 10
while x >= 0:
    print(x)
    x -= 1   

winsound.Beep(2500, 500)

# Segundo a documentação esse modulo winsound so funciona no Windows