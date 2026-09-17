print("|==================================|\n");
print("|            CALCULADORA           |\n");
print("|==================================|\n");
print("| 1. SOMA                          |\n");
print("| 1. SUBTRAÇÃO                     |\n");
print("| 3. MULTIPLICAÇÃO                 |\n");
print("| 4. DIVISÃO                       |\n");
print("| 5. SAIR                          |\n");
print("|==================================|\n");



while  True: 

    escolha = float(input("Esolha uma opção: "));

    if escolha == 5:
        print("Encerrando programa..");
        print("Programa encerrado com sucesso!");
        exit();

    elif escolha == 1:
        #função soma

    elif escolha == 2:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        subtracao = num1 - num2
        print(f"Resultade da subtração entre {num1} e {num2} é igual a: ", subtracao)
        

    elif escolha == 3:
        #função de multiplicação
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        mult = num1 * num2
        print(f"Resultade da multiplicação entre {num1} e {num2} é igual a: ", mult)

    elif escolha == 4:
        #função de divisão

    else:
        print("Opção invalida! Tente novamente...");
