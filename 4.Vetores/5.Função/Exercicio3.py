import os 
os.system("cls||clear")

def calculo(p,n):
   resultado=p * n
   return resultado

produto=float(input("Informe o preço do produto:"))

if produto>=100:
    inflacao=120/100
    
else:
    inflacao=110/100 


preçototal=calculo(produto,inflacao)

print(f"Preço Total:{preçototal:.2f}")
    
