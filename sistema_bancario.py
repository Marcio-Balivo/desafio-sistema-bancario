menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Cliente
[lc] Listar Clientes
[cc] Cadastrar Conta
[lcc] Listar Contas Correntes
[q] Sair

=> """

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return 0

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return 0

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return 0

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")
        return 0


def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            return saldo, extrato   

    else:
        print("Operação falhou! O valor informado é inválido.")
        return 0
        

def show_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("==========================================")
    print(f"Saldo R$ {saldo:.2f}")


def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):  
    if achou_cpf(usuarios, cpf):
        print(f"O CPF {cpf} já está cadastrado!")
        return 0
    else:
        usuarios.append([nome, data_nascimento, cpf, endereco])
        print("Cliente cadastrado com sucesso!")
        return usuarios
    

def criar_conta(usuarios, contas, agencia, contador_contas, cpf):
    if achou_cpf(usuarios, cpf):
        contador_contas += 1
        contas.append([contador_contas, agencia, cpf])
        return contas, contador_contas
    else:
        print("Não existe nenhum cliente com o CPF informado!")
        return 0


def achou_cpf(lista, cpf):
    for item in lista:
        for atributo in item:
            if atributo == str(cpf):
                return True
    else:
        return False
            
def listar_clientes(usuarios):
    for usuario in usuarios:
        print(f"Cliente: {usuario[0]}\t\tNascimento: {usuario[1]}\t\tCPF: {usuario[2]}\t\tEndereço: {usuario[3]}")

def listar_contas(contas):
    for conta in contas:
        print(f"Conta: {conta[0]}\tAgência: {conta[1]}\tCPF: {conta[2]}")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    contador_contas = 0

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            resposta = depositar(saldo, valor, extrato)

            if resposta:
                extrato = resposta[1]
                saldo = resposta[0]

            else:
                continue

        elif opcao == "c":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF: ")
            data_nascimento = input("Digite a data de nascimento(dd/mm/aaaa): ")
            endereco = input("Digite o endereço (Rua, numero, bairro - Cidade/Estado): ")
            
            resposta = criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

            if resposta:
                usuarios = resposta
            else:
                continue 

        elif opcao == "lc":
            print("\n================ CLIENTES ================")
            print("Nenhum cliente foi cadastrado!") if not usuarios else listar_clientes(usuarios)
            print("==========================================")


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            resposta = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

            if resposta:
                extrato = resposta[1]
                saldo = resposta[0]

            else:
                continue

        elif opcao == "cc":
            cpf = input("Digite o CPF do cliente: ")
            resposta = criar_conta(usuarios, contas, AGENCIA, contador_contas, cpf)
            if resposta:
                contador_contas = resposta[1]
                contas = resposta[0]
            else:
                continue

        elif opcao == "lcc":
            print("\n================= CONTAS ==================")
            print("Nenhuma conta foi cadastrada!") if not contas else listar_contas(contas)
            print("==========================================")

        elif opcao == "e":
            show_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()