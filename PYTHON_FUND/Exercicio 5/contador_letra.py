def check_char(text):
    type ={
        "Teste":0,
        "Lowercase":0
    }
    for char in text:
        if char.isupper():
            type["Teste"] += 1
        elif char.islower():
            type["Lowercase"] +=1
    print(f"Texto Original: {text}")
    print(f"Número de letra maiúscula: {type['Teste']}")
    print(f"Número de letra minúscula: {type['Lowercase']}")
    
check_char("A melhor forma de Pever o Futuro é Criá-lo")
    