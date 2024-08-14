import os
os.system("cls||clear")


soma=0
contador=0
while True:
   
    numero=int(input("Insira um numero:"))
    
    if numero>0:
        contador+=1
        soma+=numero
    else:
        break



  

media=soma/contador
os.system("cls||clear")
print(f"Media:{media}")

