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
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"A soma de {num1} + {num2} é: {soma}\n")

    elif escolha == 2:
        #função de subtração
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        sub = num1 - num2
        print(f"A subtração de {num1} - {num2} é: {sub}\n")

    elif escolha == 3:
        #função de multiplicação

    elif escolha == 4:
        #função de divisão

    else:
        print("Opção invalida! Tente novamente...");
