"""
Escreva um programa Python para obter uma única string de duas strings fornecidas, 
separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → **xyc abz**

"""

string1 = input("Digite uma palavra: \n")
string2 = input("Digite outra palavra: \n")

new_st1 = string2[:2] + string1[2:]
new_st2 = string1[:2] + string2[2:]

print(f"{new_st1} {new_st2}")
