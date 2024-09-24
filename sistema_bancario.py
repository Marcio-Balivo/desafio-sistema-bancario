

def display_menu():
    print(" Sistema Bancário ".center(80, "#"))
    print("".center(80, "="))
    print(" Operações ".center(80, "#"))
    print("1 - SAQUE")
    print("2 - DEPOSITO")
    print("3 - EXTRATO")
    print("0 - Sair")
    print("".center(80, "="))
    return int(input("Informe a operação desejada: "))

operacao = display_menu()