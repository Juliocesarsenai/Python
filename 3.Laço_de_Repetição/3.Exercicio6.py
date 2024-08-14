import os
os.system("cls||clear")
soma=0
nota:float=-1
for i in range(2):
    nota=float(input(f"Informe a {i+1}º nota:"))
    
    while nota<0 or nota>10:
       nota=float(input("Informe a sua nota:"))
    soma+=nota


os.system("cls||clear")
print(f"Media:{soma/2}")