#Desafio metros cúbicos

qtd_metros= int (input ("Digite a quantidade em metros cúbicos gastos: "))
valor_fixo= 26.18

if qtd_metros <=10:
    print("O valor a ser pago é de R$ 26,18")
else:
    if(qtd_metros>11) and (qtd_metros<20):
        print ("O valor a ser pago é: ", valor_fixo + 4.10) 
    else:
        if(qtd_metros >21) and (qtd_metros <30): 
            print ("O valor a ser pago é: ", valor_fixo + 10,23 )
        else:
            if (qtd_metros >=31) and (qtd_metros <50):
                print ("O valor a ser pago é: ", valor_fixo + 10.23)
            else:
                if (qtd_metros) >=50:
                    print ("O valor a ser pago é: ", valor_fixo + 11.27 )