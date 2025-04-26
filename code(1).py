# Responsáveis pelo Projeto:

# NOME                         RM

# Gabriela Queiroga          560035
# Julia Sayuri Yokoo         560541
# Maria Eduarda Ferrés       560418

########################################################################################################################

print("Seja bem vindo ao NutriKids!!!")

########################################################################################################################

# Dicionário

login = {

    "status" : "",
    "email" : "user@nutrikids.com.br",
    "senha" : "1234",

}

########################################################################################################################

# Blocos de Códigos para Login

 def employ_client():

    stats = input("Você é funcionário ou responsável? ->").strip().lower()

    while stats != "funcionario" and stats != "cliente":
        print("Informação fora do exigido! Por favor escolha dentro das opções!")
        stats = input("Você é funcionário ou responsável? ->").strip().lower()


    else:
        login["status"]  = stats
        print(login["status"])

def log_email():

    log = input("Digite o seu email ->").strip().lower()

    while True:

        if log == login["email"]:
            print(login["email"])
            break

        else:
            print("Email inválido")
            log = input("Digite o seu email ->").strip().lower()

def pass_word():

    password  = input("Digite a sua senha ->")

    while True:

        if password.isnumeric():
            int(password)

            if password == login["senha"]:
                print(login)

                print("Seja Bem Vindo!!!")
                break

            else:
                print("Senha incorreta!!!")
                password = input("Digite a sua senha ->")

        else:

            print("Por favor digite apenas números!!!")
            password = input("Digite a sua senha ->")


def log_in():

    employ_client()
    log_email()
    pass_word()

log_in()

########################################################################################################################

def milk_or_lunch():