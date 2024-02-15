import random

done = False

while not done:
    print("Qual sua escolha?")
    print("1.Adivinhe o número:")
    print("2.Sair")
    
    choice = input('>')
    
    if choice == '1':
        print("=====Adivinha um npumero de 1 a 10=====\n")
        number = int(input("Digite o número de 1 a 10:\n"))
        result = random.randint(1,10)
        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f'Tente Novamente. O número sorteado foi {result}')
    elif choice == "2":
        done = True
    else:
        print("Opção inválida.Escolha uma opção entre 1 e 2")