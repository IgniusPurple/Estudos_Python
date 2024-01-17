"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.

"""

salary = float(input("Qual é o seu salário:\n\n"))
per_increase = 0.15

if salary > 1250:
    per_increase = 0.10

increase = salary * per_increase
newSalary = increase+salary

print(f"\nSeu aumento de salário foi de R$ {increase} passando assim seu salário para R$ {newSalary}")