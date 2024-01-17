import strings


name = str(input("Digite uma frase:\n"))

print(f'\nAqui está sua frase invertida: {strings.inverse(name)}\n')
print(f'\nAqui está os caracteres pares: {strings.even_characteres(name)}\n')
print(f'\nAqui está os caracteres impares: {strings.odd_characteres(name)}\n')