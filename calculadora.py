def subtracao():
    num1 = float(input("Valor A: "))
    num2 = float(input("Valor B: "))

    subtracao = num1 - num2

    print(f"===> Resultado: {subtracao}\n")

print("|==================================|\n");
print("|            CALCULADORA           |\n");
print("|==================================|\n");
print("| 1. SOMA                          |\n");
print("| 2. SUBTRAÇÃO                     |\n");
print("| 3. MULTIPLICAÇÃO                 |\n");
print("| 4. DIVISÃO                       |\n");
print("| 5. SAIR                          |\n");
print("|==================================|\n");



while  True: 

    escolha = float(input("Esolha uma opção: "));

    if escolha == 5:
        print("Encerrando programa..");
        print("Programa encerrado com sucesso!");
        exit()

    elif escolha == 1:
        soma()

    elif escolha == 2:
        subtracao()

    elif escolha == 3:
        multipicacao()

    elif escolha == 4:
        divisao()

    else:
        print("Opção invalida! Tente novamente...");
