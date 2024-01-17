"""Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário"""

number = int(input("Tabuada de: \n"))
firstNumber = int(input("De:\n"))
lastNumber = int(input("Até:\n"))

x = firstNumber

while x <= lastNumber :
    print (f"\n{number} x {x} = {number * x}")
    x += 1

