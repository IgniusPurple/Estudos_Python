import math

# 1 - Accessar o número Pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 -  Acessar o número de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondando números para cima e baixo
num1 = 10.4
print(math.ceil(num1))
print(math.floor(num1))

# 4 - Fatorial de um número 
num2 = print(input("Digite um número para o fatorial:\n"))
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(5,5))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC (Maior Divisor Comum)
mdc = math.gcd(25,100) # 25/100 
print(mdc)

# 8 - Logaritmo
print(math.log(10))