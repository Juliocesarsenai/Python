import os

os.system("cls||clear")

n1=int(input("Primeiro Numero:"))
n2=int(input("Segundo Numero:"))

maiornumero=0
menornumero=999

os.system("cls||clear")
print(f"Primeiro Numero:{n1}")
print(f"Segundo Numero:{n2}")
print(f"Soma:{n1+n2}")
print(f"Produto:{n1*n2}")
print(f"Media: {(n1+n2)/2}")


if n1>n2:
    maiornumero=n1
    menornumero=n2

else:
    maiornumero=n2
    menornumero=n1


print(f"Maior Numero:{maiornumero}")
print(f"Menor Numero:{menornumero}")



