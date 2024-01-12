menu = """


[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        exc_saldo = valor > saldo

        exc_limite = valor > limite

        exc_saques = numero_saques >= LIMITE_SAQUES

        if exc_saldo:
            print('Saldo insuficiente. Saque não realizado.')

        elif exc_limite:
            print('Limite diário de saques atingido. Saque não realizado.')

        elif exc_saques:
            print('Limite máximo por saque é de R$500,00. Saque não realizado.')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print(" O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Por favor selecione a operação desejada.")
