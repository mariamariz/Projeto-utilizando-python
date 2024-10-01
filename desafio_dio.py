menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 5000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":  # Depositar
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, insira um valor numérico válido.")

    elif opcao == "2":  # Sacar
        try:
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Por favor, insira um valor numérico válido.")

    elif opcao == "3":  # Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":  # Sair
        print("Obrigado por escolher o nosso sistema, até a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
