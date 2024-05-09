import os
os.system("cls||clear")


i=0
soma=0
numerospares=0
numerosimpares=0
somadenumerospares=0



while True:
    numero=int(input("Escolha um numero:"))
    if numero>0:
        i+=1
        soma+=numero

        if numero%2==0:
             numerospares+=1
             somadenumerospares+=numero
        else:
            numerosimpares+=1
    if numero==0:
        media=soma/i
        mediadenumerospares=somadenumerospares/numerospares  
        os.system("cls||clear")
        print(f"Quantidade de Numeros Pares:{numerospares}")
        print(f"Quantidade de Numeros Impares:{numerosimpares}")
        print(f"Media de Numeros Pares:{mediadenumerospares}")
        print(f"Media Geral:{media}")
        break






