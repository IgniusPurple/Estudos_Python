# Escreva um programa em Python que leia quatro números e calcule a média entre esses números


note1 = float(input("Digite a sua nota do Primeiro Bimestre: "))
note2 = float(input("Digite a sua nota do Segundo Bimestre: "))
note3 = float(input("Digite a sua nota do Terceiro Bimestre: "))
note4 = float(input("Digite a sua nota do Quarto Bimestre: "))

avarege = (note1 + note2 + note3 + note4) / 4

print(f"\nSua média no ano foi: {avarege: .2f}")
