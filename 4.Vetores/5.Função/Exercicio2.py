import os

os.system("cls||clear")

def tabuada(n,contador):
    resultado=n * contador
    return resultado

numero=int(input("Escolha um numero:"))

#Tabuada
os.system("cls||clear")
for i in range(1,11):

    resultadodatabuada=tabuada(numero,i)
    print(f"{numero}x{i}:{resultadodatabuada}")

