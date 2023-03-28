def espaço():
    print("="*15)

menu="""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
Limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor=float(input("informe o valor do deposito"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ { valor:.2f}\n"
            
        else:
            print("operação falhouo valor informado e invalido.")
        
    elif opcao =="s":
        
        valor=float(input("informe o valor do saque"))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saques >= Limite_saques
        
        if excedeu_saldo:
            print("operação falhou voce nao tem saldo o suficiente")
            
        elif excedeu_limite:
            print(" operacao falhou o valor do saque exede o limite")
        
        elif excedeu_saque:
            print(" operacao falhou numero de saques exedidos")
            
        elif valor > 0:
            saldo -= valor
            extrato += f" saque R$ {valor:.2}\n"
            numero_saques += 1
            
        else:
            print(" operacao falou o valor informado e invalido")
            
        
    elif opcao == "e":
        
        print("===============EXTRATO===============")
        print("nao foram realizados movimentações" if not extrato else extrato)
        print(f"saldo: R$ `{ saldo:.2f}")
        print("="*30)
        
    elif opcao == "q":
        break
    
    
    else:
        print("operacao invalida por favor selecione novamente a operação desejada")
        
