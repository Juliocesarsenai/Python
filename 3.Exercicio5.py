import os
os.system("cls||clear")

nota=float(input("Informe a sua nota:"))

while nota<0 or nota>10:
    os.system("cls||clear")

    print("ERRO.Tente Novamente")
    nota=float(input("Informe a sua nota:"))


os.system("cls||clear")
print(f"Nota:{nota}")



