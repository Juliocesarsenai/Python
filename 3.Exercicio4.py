import os
os.system("cls||clear")

soma=0

for i in range(3):

    notas=float(input(f"Informe a {i+1}º nota:"))
    soma+=notas

media=soma/3

os.system("cls||clear")
print(f"Media:{media}")
if(media>7):
    print("Aprovado!")

if(media<7 and media >=4):
    print("Recuperação!")

if(media<4):
    print("Reprovado!")

