def divisao():
    a = float(input("Valor A: "))
    b = float(input("Valor B: "))
    
    if b < 0 or b == 0 :
        print("Não e possivel dividir por 0")

    else:
        divisao = a / b
        print(f"===> Resultado: {divisao}")


while  True: 

    print("|==================================|\n")
    print("|            CALCULADORA           |\n")
    print("|==================================|\n")
    print("| 1. SOMA                          |\n")
    print("| 1. SUBTRAÇÃO                     |\n")
    print("| 3. MULTIPLICAÇÃO                 |\n")
    print("| 4. DIVISÃO                       |\n")
    print("| 5. SAIR                          |\n")
    print("|==================================|\n")


    escolha = float(input("Esolha uma opção: "))

    if escolha == 5:
        print("Encerrando programa..")
        print("Programa encerrado com sucesso!")
        exit()

    elif escolha == 1:
        soma()

    elif escolha == 2:
        subtracao()

    elif escolha == 3:
        multiplicacao()

    elif escolha == 4:
        divisao()

    else:
        print("Opção invalida! Tente novamente...")
