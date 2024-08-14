import os
os.system("cls||clear")

quantidade_numeros:int=0
soma=0
while True:
    numero=int(input("Escolha um numero:"))

    if numero>0:
        quantidade_numeros+=1
        soma+=numero
    else:
        break
    
#Calcular a media

os.system("cls||clear")
media=soma/quantidade_numeros

print(f"Media:{media}")



    

