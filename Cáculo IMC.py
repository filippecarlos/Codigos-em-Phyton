#Cáculo do imc

nome=(input ("Digite seu nome completo: "))
idade=int(input ("Digite sua idade: "))
gênero= str (input ("Digite seu gênero: "))
peso=float (input ("Digite o seu peso: "))
altura=float (input ("Digite a sua altura: "))

r= (peso)/(altura**2)

if (r<=18.5):
    print (nome , gênero, idade, "anos", "Seu imc é: ", r , "Você está abaixo do peso.")
    
if (r>=19.0) and (r<=24.9):
    print (nome , gênero, idade, "anos", "Seu imc é: ", r , "Você está com seu peso normal.")

if (r>=25.0) and (r<=29.9):
    print (nome , gênero, idade, "anos", "Seu imc é: ", r , "Atenção você está com sobrepeso.")

if (r>=30.0) and (r<=34.9):
    print (nome , gênero, idade, "anos", "Seu imc é: ", r , "Cuidado você está com obesidade grau 1.")

if (r>=35.0) and (r<=39.9):
    print (nome , gênero, idade, "anos", "Seu imc é: ", r , "Cuidado você está com obesidade grau 2.")

if (r>=40.0):
    print (nome , gênero, idade, "anos", "Seu imc é: ", r , "Corre você está com obesidade grau 3 e pode morrer.")