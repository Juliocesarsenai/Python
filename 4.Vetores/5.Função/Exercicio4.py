import os
os.system("cls||clear")

print("==MENU==")
print("1-Domingo \n2-Segunda \n3-Terça \n4-Quarta \n5-Quinta \n6-Sexta \n7-Sabado")

opcao=input("\nEscolha uma opção:")

os.system("cls||clear")
match(opcao):
    
    case '1':
        print("Final de Semana")
        print("Domingo!")
    case '2':
        print("Dia Util")
        print("Segunda!")
    case '3':
        print("Dia Util")
        print("Terça!")
    case '4':
        print("Dia Util")
        print("Quarta!")
    case '5':
        print("Dia Util")
        print("Quinta!")
    case '6':
        print("Dia Util")
        print("Sexta!")
    case '7':
        print("Sabado")
        print("Final de Semana")
    case _:
        input("Opção Invalida!")
        
