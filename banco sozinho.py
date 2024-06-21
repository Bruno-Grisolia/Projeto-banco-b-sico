menu = """==========MENU==========
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
====================================
>>"""
saldo = 0
limite_por_saque = 500
numero_saque = 0
limite_saque_diario = 3
extrato = ""

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Digite um valor de depósito!\n"))

        if valor > 0:
            saldo += valor
            extrato += f'O valor do depósito é de R$: {valor: .2f}\n'
        else:
            print ("Operação falhou ! Valor informado é inválido\n")

    elif opcao == "2":
        valor = float(input("Digite o valor do seu saque\n"))
        
        excedeu_saldo = valor>saldo
        excedeu_limite_por_saque = valor > limite_por_saque
        excedeu_limite_saque_diario = numero_saque >= limite_saque_diario

        if excedeu_saldo:
            print("Operação falhou ! Valor insuficiente.\n")

        elif excedeu_limite_por_saque:
            print("Operação falhou ! Você excedeu o valor do limite por saque.\n")

        elif excedeu_limite_saque_diario:
            print("Operação falhou ! Você excedeu o limite diário de saque.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$: {valor:.2f}\n'
            numero_saque += 1
        else:
            print ("Operação falhou ! O valor do saque é inválido\n")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print ("Não foram realizadas movimentações na sua conta.\n" if not extrato else extrato)
        print(f'Saldo: R$: {saldo: .2f}\n')
        print ("=============================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, digite novamente a opção desejada.")
        

        