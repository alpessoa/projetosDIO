menu = ''' #### Banco DIO ####

Selecione a opção desejada: 

[1] Criar Usuário
[2] Criar Conta
[3] Listar Contas
[4] Depositar
[5] Sacar
[6] Extrato
[7] Sair

=> '''
usuarios = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

def depositar(deposito, saldo, extrato,/):
    if deposito > 0:
            saldo += deposito
            extrato += f"Deposito no valor de R$ {deposito:.2f}\n"
            print("Deposito efetuado com sucesso!")
    else:
        print("Valor inválido!")

    return saldo, extrato

def sacar(*, saque, numero_saques, limite_saques, saldo, extrato):

    if saque > limite:
        print("Valor para saque excedeu o limite!\n")
    
    elif saque > saldo:
        print("Saldo insuficiente!\n")
        
    elif numero_saques >= limite_saques:
        print("Limite diario de saque excedido!\n")
    
    elif saque >0:
        extrato += f"Saque no valor de R$ {saque:.2f}\n"
        numero_saques +=1
        saldo -= saque

    else:
        print("Comando invalido!")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/,*, extrato):
    if extrato == "":
        print("Não foram realizadas movimentações.\n")
    else:
        print(f"{extrato}\n Saldo Total R$ {saldo:.2f}\n")

def filtro_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_usuarios(usuarios):
    cpf = input("Informe seu cpf (apenas numeros): ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("CPF já possui cadastro em sistema!")

    nome = input("Informe seu nome completo: ")
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (logradouro, numero - bairro - cidade/sigla do estado): ")
    
    usuarios.append({"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco})

    print("Usuario cadastrado com sucesso!")

def criar_contas(agencia, conta, usuarios):
    cpf = input("Digite o cpf do usuario (Apenas numeros): ")
    usuario = filtro_usuarios(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "conta": conta, "usuario": usuario}
    print("Usuario nao encontrado.")

def listar_contas(contas):
    for conta in contas:
        dados = f'''
        Agencia: {conta['agencia']}
        C/c: {conta['conta']}
        Titular: {conta['usuario']['nome']}
**************************************************************
'''
        print(dados)

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        print("###Criar Usuario###")
        criar_usuarios(usuarios)

    elif opcao == 2:
        print("###Criar Conta###")
        nova_conta = len(contas) + 1
        conta = criar_contas(AGENCIA, nova_conta, usuarios)

        if conta: 
            contas.append(conta)

    elif opcao == 3:
        listar_contas(contas)

    elif opcao == 4:
        print("###Deposito###")
        deposito = float(input("Informe o valor a ser depositado: R$ "))

        saldo, extrato = depositar(deposito, saldo, extrato)  

    elif opcao == 5:
        print("###Saque###\n")
        saque = float(input("Informe o valor a ser sacado: R$ "))

        saldo, extrato, numero_saques = sacar(saque=saque,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES,saldo=saldo,extrato=extrato)

    elif opcao == 6:
        print("###Extrato###\n")
        exibir_extrato( saldo, extrato=extrato)

    elif opcao == 7:
        print("Obrigado por usar o Banco DIO!")
        break

    else:
        print("Comando inválido. Por favor selecione a operação desejada.\n")
