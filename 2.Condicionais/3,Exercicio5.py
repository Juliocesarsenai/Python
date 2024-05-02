import os

os.system("cls||clear")

numerospares=0
numerosimpares=0


for i in range(0,5):
    numero=int(input(f"{i+1}º numero:"))

    if numero%2==0:
        numerospares+=1
 
    else:
        numerosimpares+=1


print(f"Numeros Pares:{numerospares}")
print(f"Numeros Impares:{numerosimpares}")
 