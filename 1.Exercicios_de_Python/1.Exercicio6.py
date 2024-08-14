import os

os.system("cls||clear")

nome=str(input("Nome:"))
sexo=str(input("Sexo(M/F):"))
estadocivil=str(input("Estado Civil(Solteiro ou Casado):"))



if sexo=="F" and estadocivil=="Casada":
    tempodecasada=str(input("Informe o seu tempo de casada em anos:"))

    os.system("cls||clear")
    print(f"Nome:{nome}")
    print(f"Sexo:{sexo}")
    print(f"Estado Civil:{estadocivil}")
    print(f"Tempo de Casada:{tempodecasada}")

else:
    print(f"Nome:{nome}")
    print(f"Sexo:{sexo}")
    print(f"Estado Civil:{estadocivil}")





