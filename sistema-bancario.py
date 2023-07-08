saldo_disponivel = 0
total_sacado = 0
saques_efetuados = 0
total_depositado = 0

while True:
    operacao = input("""Bem vindo ao LuizBank, as operações disponíveis estão listadas abaixo:
    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Sair do programa\n""")

    if operacao == '1':
        valor_deposito = float(input("Digite um valor para depósito: "))
        if valor_deposito > 0:
            total_depositado += valor_deposito
            saldo_disponivel += valor_deposito
            print("Depósito efetuado com sucesso!\n")
        else:
            print("Digite um valor válido\n")
    elif operacao == '2':
        if saques_efetuados == 3:
            print("Você atingiu o limite diário de 3 saques.\n")
        else:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 500.00:
                print("O limite por saque é 500 R$\n")
            elif valor_saque <= 0:
                print("Valor inválido\n")
            elif valor_saque > saldo_disponivel:
                print("Você não tem saldo disponível para realizar a operação\n")
            else:
                total_sacado += valor_saque
                saldo_disponivel -= valor_saque
                saques_efetuados += 1
                print("Saque efetuado com sucesso!\n")
    elif operacao == '3':
        print(f"""==================EXTRATO==================
    Valor depositado = {total_depositado:.2f}
    Valor sacado = {total_sacado:.2f}
    Saldo disponível em conta = {saldo_disponivel:.2f}
===========================================\n""")
    elif operacao == '4':
        print("Até a próxima!!\n")
        break
    else:
        print("Opção inválida, favor escolher novamente.\n")
