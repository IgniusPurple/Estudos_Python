"""

*args -  Utilizamos ele quando não temos certeza de quantos argymentos
queremos ter numa função.
- Os argumentos são passados como tupla

**kwargs - Além dos valpores podems passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como dicinário

"""

# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7, 8, 8, 9)
sum(7, 8 ,9 ,10 ,11 ,20)


# 2 -  Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("#####CURSO#######")
presentation(name = "Python", category = "Backend", level = "Iniciante")
presentation(name = "Visão Computacional Python", category = "IA", level = "Avançado")
presentation(name = "Dashborads com Dash", category = "Data Science", level = "Intermediário")
        
