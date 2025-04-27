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
 def employ_client():

    stats = input("Você é funcionário ou responsável? ->").strip().lower()



@@ -59,22 +59,33 @@ def pass_word():

    while True:

        if
        if password == login["senha"]:
            print(login)
        if password.isnumeric():
            int(password)

            print("Seja Bem Vindo!!!")
            break
            if password == login["senha"]:
                print(login)

                print("Seja Bem Vindo!!!")
                break

            else:
                print("Senha incorreta!!!")
                password = input("Digite a sua senha ->")

        else:
            print("Senha incorreta!!!")

            print("Por favor digite apenas números!!!")
            password = input("Digite a sua senha ->")


def log_in():

    employ_client()
    log_email()
    pass_word()

log_in()

########################################################################################################################
########################################################################################################################

ef milk_or_lunch():
def clean_number(text):
    # Ensures only valid numbers are returned
    allowed = "0123456789."
    cleaned = ''.join([char for char in text if char in allowed])
    if cleaned == '' or cleaned == '.':
        raise ValueError("Entrada inválida: nenhum número encontrado!")
    return cleaned


def quiz():
    questions = [
        "Qual o peso do bebê (kg)? ",
        "Qual o comprimento/tamanho do bebê (cm)? ",
        "Quantos dias de vida o bebê tem? ",
        "Quantas mamadas por dia? "
    ]

    answers = []

    for question in questions:
        while True:
            answer = input(question)
            if answer.strip():  # If answer is not empty
                answers.append(answer)
                break
            else:
                print("Por favor, preencha este campo corretamente.")

    return answers


def calculate_lactary(data):
    try:
        # Extracting and converting the input data
        weight = float(clean_number(data[0]))
        length = float(clean_number(data[1]))  # Not used at the moment
        age_days = int(clean_number(data[2]))  # Not used at the moment
        feedings_per_day = int(clean_number(data[3]))

        # Define a default volume per kg (for example, 150 ml/kg/day)
        volume_per_kg = 150

        # Volume calculation
        total_volume_per_day = weight * volume_per_kg
        volume_per_feeding = total_volume_per_day / feedings_per_day

        return total_volume_per_day, volume_per_feeding
    except IndexError:
        raise ValueError("Todos os campos precisam ser preenchidos corretamente.")


def choose_unit():
    print("\nComo você gostaria de ver o resultado?")
    print("(1) Mililitros (ml)")
    print("(2) Litros (L)")

    while True:
        choice = input("Digite 1 ou 2: ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")


def main():
    print("=== Questionário do Lactário ===")
    try:
        baby_data = quiz()
        total_volume, volume_feeding = calculate_lactary(baby_data)

        unit = choose_unit()

        print("\n=== Resultado do Cálculo ===")
        if unit == "1":
            print(f"Volume total por dia: {total_volume:.1f} ml")
            print(f"Volume por mamada: {volume_feeding:.1f} ml")
        else:
            print(f"Volume total por dia: {total_volume / 1000:.3f} L")
            print(f"Volume por mamada: {volume_feeding / 1000:.3f} L")

    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()

########################################################################################################################
def escolher():
    resposta = input(
        "Você deseja usar o [1]Cardapio Inteligente ou a [2]Calculadora de Lactario? (Por favor digite apenas o número das opções)\n ->")

    if resposta == 1:

        print("Seja Bem vinda!!!"
              "Por favor responda o questionário:")

        resposta == cardapio_inteligente()

    elif resposta == 2:

        print("Seja Bem vinda!!!"
              "Por favor responda o questionário:")

        resposta == calculadora_lactario()


def cardapio_inteligente():
    dic = {

    }
