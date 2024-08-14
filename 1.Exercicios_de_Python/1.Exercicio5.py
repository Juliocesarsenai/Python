import os
os.system("cls||clear")

produto=str(input("Nome do Produto:"))
precodoproduto=float(input("Preço do Produto:"))
quantidade=int(input("Quantidade do produto:"))

if quantidade <=5:
    print(f"Preço Total:{precodoproduto*quantidade * 98/100}")

if quantidade>5 and quantidade<=10:
    print(f"Preço Total:{precodoproduto*quantidade * 97/100}")

if quantidade>10:
    print(f"Preço Total:{precodoproduto*quantidade * 95/100}")

