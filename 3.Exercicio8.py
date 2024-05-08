import os
os.system("cls||clear")

i=0
soma=0
quantidadedenotas=0

while True:
   

    print("=========Menu=========")
    print("S-Inserir mais uma nota")
    print("P-Ver quantas notas foram inseridas")
    print("N-Calcular a media aritmetica das notas informadas")
    opcao=str(input("Escolha uma das opções:"))
    

    if opcao=="S":
        nota=float(input("Insira a nota:"))
        quantidadedenotas+=1
        soma+=nota
        i+=1
        

    if opcao=="P":
        print(f"Notas Inseridas:{quantidadedenotas}")

    if opcao=="N":
        media=soma/i+1
        print(f"Media:{media}")
