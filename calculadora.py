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
        #função de subtração

    elif escolha == 3:
        #função de multiplicação

    elif escolha == 4:
        #função de divisão

    else:
        print("Opção invalida! Tente novamente...");
