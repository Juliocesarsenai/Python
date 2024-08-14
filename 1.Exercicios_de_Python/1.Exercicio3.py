import os

os.system("cls||clear")

login=str(input("Digite o seu login:"))
senha=str(input("Digite a sua senha:"))

logincorreto="juliocesar2005@gmail.com"
senhacorreta="julio2005"


os.system("cls||clear")
if login==logincorreto and senha==senhacorreta:
    print("Bem vindo!")

else :
    print("Login ou Senha Invalidos")


