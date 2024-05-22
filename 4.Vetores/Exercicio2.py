import os

os.system("cls||clear")
numeros=[]
i=0
numerospares=0
numerosimpares=0
for i in range(6):
    numero=int(input("Digite o numero:"))
    numeros.append(numero)

    if numero%2==0:
        numerospares+=1
    else:
        numerosimpares+=1

os.system("cls||clear")
for i,numero in enumerate(numeros):
    print(f"{i+1}º Numero:{numeros[i]}")

print(f"Quantidade de Numeros Pares:{numerospares}")
print(f"Quantidade de Numeros Impares:{numerosimpares}")