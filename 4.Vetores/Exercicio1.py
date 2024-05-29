import os
os.system("cls||clear")

notas=[]
i=0
soma=0
maiornumero=0
menornumero=9999
for i in range(5):
    
    nota=float(input(f"Digite fa sua nota: "))
    notas.append(nota)

    maiornumero=max(notas)
    menornumero=min(notas)
        
    
#Exibindo resultados
os.system("cls||clear")
for i in range(5):
    print(f"Notas:{notas[i]}")

print(f"Maior Nota:{maiornumero}")
print(f"Menor Nota:{menornumero}")        
    
    