import os
os.system("cls||clear")

while True:
    print("======MENU======")
    print("1.PICANHA \n2.LASANHA \n3.STROGONOFF \n4.BIFE-ACEBOLADO \n5.PÃO COM OVO ")
    

    opcao=input("Escolha um prato:")

    match(opcao):
        case '1':
            print("Picanha \nValor:25 reais")
            break
        case '2':
            print("Lasanha\nValor:20 reais")        
            break
        case '3':
            print("Strogonoff \nValor:18 reais")
            break
        case '4':
            print("Bife Acebolado \nValor:15 reais")
            break
        case '5':
            print("Pão com Ovo \nValor:5 reais") 
            break
        case _:
            print("Opção Invalida")   
          
