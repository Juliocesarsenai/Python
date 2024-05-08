import os
os.system("cls||clear")

notas:float=-1
soma=0
for i in range(3):
    notas=float(input(f"Informe a {i+1}º nota:"))
    soma+=notas

while True:
    if notas>10 or notas<0:
        print("ERRO.TENTE NOVAMENTE")
    else:
        break

media=soma/3
print(f"Media:{media}")

if media>=7:
   print ("Aprovado!")
if media<7 and media>=5:
   print ("Em recuperação!")
if media<5:
   print("Reprovado!")

   
