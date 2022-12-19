print("==== EXERCICIO 044 ====")
print("==== LOJAS CARLÃO =====")
valor = float(input("VALOR TOTAL: R$ "))
escolha = int(input('''DIGITE UMA DAS FORMAS DE PAGAMENTO ABAIXO:
 [1] A VISTA DINHEIRO/CHEQUE.
 [2] A VISTA CARTÃO.
 [3] 2X NO CARTÃO.
 [4] 3X OU MAIS NO CARTÃO.
 OPÇÃO DE PAGAMENTO: '''))
print("=" * 25)
if escolha == 1:
    nvalor = valor - ((valor*10)/100)
    print('''COMPRAS A VISTA NO DINHERIO/CHEQUE COM 10% DE DESCONTO:
    VALOR DA COMPRA: R${}
    TOTAL A PAGAR: R${}'''.format(valor, nvalor))
elif escolha == 2:
    nvalor = valor - ((valor*5)/100)
    print('''COMPRAS A VISTA NO CARTÃO COM 5% DE DESCONTO: 
    VALOR DA COMPRA: R${}
    TOTAL A PAGAR: R${}'''.format(valor, nvalor))
elif escolha == 3:
    parcelas = valor/2
    print('''COMPRAS EM 2X NO CARTÃO SEM JUROS:
    VALOR A PAGAR: R${}
    VALOR DAS PARCELAS: R${}'''.format(valor, parcelas))
elif escolha == 4:
    nvalor = valor + ((valor * 20) / 100)
    nparcelas = int(input("DIGITE O NUMERO DE PARCELAS (ATÉ 12X): "))
    if 12 >= nparcelas >= 3:
        parcelas = nvalor/nparcelas
        print('''COMPRAS EM 3X OU MAIS NO CARTÃO COM 20% DE JUROS:
        VALOR DA COMPRA: R${}
        TOTAL A PAGAR: R${}
        VALOR DAS PARCELAS: {}X DE R${}'''.format(valor, nvalor, nparcelas, parcelas))
    else:
        print("NUMERO DE PARCELAS INVALIDO.")
else:
     print("FORMA DE PAGAMENTO INVALIDA.")
