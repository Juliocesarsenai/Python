import os

os.system("cls||clear")

nome=str(input("Nome do aluno:"))
idade=int(input("Idade do aluno:"))
nota1=float(input("Digite a sua primeira nota:"))
nota2=float(input("Digite a sua segunda nota:"))
nota3=float(input("Digite a sua terceira nota:"))

os.system("cls||clear")
media=(nota1+nota2+nota3)/3
print(f"Nome:{nome}")
print(f"Idade:{idade}")
print(f"Primeira Nota:{nota1}")
print(f"Segunda Nota:{nota2}")
print(f"Terceira Nota:{nota3}")
print(f"Media:{media}")

if media<7:
    print("Situação:Reprovado!")

else:
    print("Situação:Aprovado!")