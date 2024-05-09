import os
os.system("cls||clear")
 

maioridade=0
menoridade=999
somadesalario=0
mulherescom5000=0
i=0

opcao=1


while opcao==1:
    print("====MENU====")
    print("1.Adicionar Pessoa")
    print("2.Exibir resultados e sair")

    opcao=int(input("Opção:"))
    match opcao:
        case 1:
            os.system("cls||clear")
            nome=str(input("Informe o nome:"))
            idade=int(input("Informe a idade:"))
           

            while idade<0: 
                print("ERRO.TENTE NOVAMENTE")
                idade=int(input("Informe a idade:"))
           
            sexo=str(input("Informe o sexo M/F:"))
            sexo=sexo.upper()
            while sexo!="M" and sexo!="F":
                print("ERRO.TENTE NOVAMENTE")
                sexo=str(input("Informe o sexo M/F:"))


            salario=float(input("Informe o seu salario:"))

            while salario<0: 
                print("ERRO.TENTE NOVAMENTE")
                salario=float(input("Informe o seu salario:"))

            somadesalario+=salario
            i+=1

            if salario<0 or idade<0:
                print("ERRO.TENTE NOVAMENTE")
                break


            if sexo=="F" and salario>=5000:
                mulherescom5000+=1

            if idade>maioridade:
                maioridade=idade
            if idade<menoridade:
                menoridade=idade


        case 2:
            os.system("cls||clear")
            print(f"Quantidade de mulheres com salario a partir de 5000:{mulherescom5000}")
            print(f"Maior Idade:{maioridade}")
            print(f"Menor Idade:{menoridade}")
            mediasalarial=somadesalario/i
            print(f"Media salarial:{mediasalarial}")
                    
