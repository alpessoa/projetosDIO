menu = ''' #### Banco DIO ####

Selecione a opção desejada: 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("###Deposito###")
        deposito = float(input("Informe o valor a ser depositado: R$ "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito no valor de R$ {deposito:.2f}\n"
        else:
            print("Valor inválido!")
    elif opcao == 2:
        print("###Saque###\n")
        saque = float(input("Informe o valor a ser sacado: R$ "))

        if numero_saques < limite_saques and saque <= limite and saldo > saque and saque >0:
            extrato += f"Saque no valor de R$ {saque:.2f}\n"
            numero_saques +=1
            saldo -= saque

        elif saque > limite:
            print("Valor para saque excedeu o limite!\n")
        
        elif saque > saldo:
            print("Saldo insuficiente!\n")
        
        elif numero_saques >= limite_saques:
            print("Limite diario de saque excedido!\n")
        
        else:
            print("Comando invalido!")

    elif opcao == 3:
        print("###Extrato###\n")
        if extrato == "":
            print("Não foram realizadas movimentações.\n")
        else:
            print(f"{extrato}\n Saldo Total R$ {saldo:.2f}\n")
    elif opcao == 4:
        print("Obrigado por usar o Banco DIO!")
        break

    else:
        print("Comando inválido. Por favor selecione a operação desejada.\n")
