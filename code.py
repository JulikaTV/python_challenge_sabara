# Responsáveis pelo Projeto:

# NOME                         RM

# Gabriela Queiroga          560035
# Julia Sayuri Yokoo         560541
# Maria Eduarda Ferrés       560418

########################################################################################################################

print("Seja bem-vindo ao NutriKids!!!")  # Exibe a mensagem de boas-vindas

# Dicionário de login
login = {

    "status": "",  # Armazena o status do usuário (funcionário ou responsável)
    "email": "user@nutrikids.com.br",  # Email do usuário para login
    "senha": "1234",  # Senha do usuário para login

    }

# Dicionário de permissões
permissions = {

    "funcionario": ["criar", "editar", "visualizar"],  # Permissões para o funcionário
    "responsavel": ["visualizar"]  # Permissões para o responsável

    }

# Dicionário que armazena dados modificados pelo profissional
dados_modificados = {

    "nome_da_crianca": "",  # Nome da criança
    "recomendacao": "",  # Tipo de recomendação
    "volume_prescrito": "",  # Volume prescrito por mamada e por dia
    "observacoes": ""  # Observações clínicas

    }

# ---------------------- Funções de Autenticação -----------------------

def employ_client():

    #Função para verificar se o usuário é funcionário ou responsável.
    #Solicita ao usuário que informe o seu status e valida a resposta.

    while True:

        stats = input("Você é funcionário ou responsável? -> ").strip().lower()  # Pergunta o status do usuário

        if stats in ['funcionario', 'responsavel']:  # Se a resposta for válida
            print(f"\nSeja bem-vindo(a), {stats}!\n")  # Mensagem de boas-vindas
            login['status'] = stats  # Armazena o status do usuário no dicionário de login
            break  # Sai do loop

        else:
            print("Por favor, digite apenas 'funcionário' ou 'responsável'.")  # Mensagem de erro

def log_email():

    #Função para validar o email do usuário durante o login.
    #Solicita que o usuário insira o seu email e verifica se é o correto.

    while True:

        email = input("Por favor, digite o seu email:\n-> ").strip()  # Solicita o email

        if email == login["email"]:  # Verifica se o email está correto
            print("\nEmail correto! Por favor, prossiga.\n")  # Mensagem de sucesso
            break  # Sai do loop

        else:
            print("\nO email que você digitou está incorreto. Tente novamente.")  # Mensagem de erro

def pass_word():

    #Função para validar a senha do usuário durante o login.
    #Solicita que o usuário insira a senha e verifica se é a correta.

    while True:

        password = input("Digite a sua senha -> ").strip()  # Solicita a senha

        if not password.isnumeric():  # Verifica se a senha contém apenas números
            print("Por favor, digite apenas números!")  # Mensagem de erro

        elif password == login["senha"]:  # Verifica se a senha está correta
            print("Senha correta! Seja bem-vindo!!!")  # Mensagem de sucesso
            break  # Sai do loop

        else:
            print("Senha incorreta! Tente novamente.")  # Mensagem de erro

def log_in():

    #Função de login, chama as funções de autenticação para verificar o status do usuário, email e senha.

    employ_client()  # Chama a função de autenticação de status
    log_email()  # Chama a função de validação do email
    pass_word()  # Chama a função de validação da senha
    return permissions.get(login["status"], [])  # Retorna as permissões de acordo com o status do usuário

def logout():

    #Função para realizar o logout do usuário, limpando o status.

    print(f"\n{login['status'].capitalize()} desconectado com sucesso!\n")  # Mensagem de desconexão
    login['status'] = ""  # Reseta o status do login

# ---------------------- Questionário e Cálculo -----------------------

# Lista do questionário
quiz_lac = [

    ['Nome', ''],
    ['Idade', 0],
    ['Peso', 0.0],
    ['Sexo', ''],
    ['Tipo de Alimentação', ''],
    ['Fórmula ( se aplicável )', ''],
    ['Frequência de mamadas ( por dia )', 0],
    ['observações Clínicas', '']

]

def quiz():

    #Função que solicita e preenche as informações do questionário.
    #Recebe dados como nome, idade, peso, tipo de alimentação, entre outros.

    for i in range(len(quiz_lac)):

        while True:

            resposta = input(f"{quiz_lac[i][0]}: ").strip()  # Solicita uma resposta para cada campo do questionário

            if resposta:  # Verifica se a resposta não está vazia

                # Converte os dados de acordo com o tipo do campo
                if quiz_lac[i][0] == 'Idade':
                    quiz_lac[i][1] = int(resposta)  # Converte a resposta para inteiro

                elif quiz_lac[i][0] == 'Peso':
                    quiz_lac[i][1] = float(resposta)  # Converte a resposta para float

                elif quiz_lac[i][0] == 'Frequência de mamadas ( por dia )':
                    quiz_lac[i][1] = int(resposta)  # Converte a resposta para inteiro

                else:
                    quiz_lac[i][1] = resposta  # Armazena a resposta como string
                break  # Sai do loop

            else:
                print("Por favor, preencha este campo corretamente.")  # Mensagem de erro se o campo estiver vazio

def choose_unit():

    #Função para que o usuário escolha a unidade de medida para o volume.
    #Oferece a opção de escolher entre mililitros (ml) ou litros (L).

    print("\nComo você gostaria de ver o resultado?")  # Exibe a pergunta sobre a unidade de medida
    print("(1) Mililitros (ml)")  # Opção 1: mililitros
    print("(2) Litros (L)")  # Opção 2: litros

    while True:
        choice = input("Digite 1 ou 2: ")  # Solicita a escolha do usuário

        if choice in ["1", "2"]:  # Verifica se a escolha é válida
            return choice  # Retorna a escolha do usuário

        else:
            print("Opção inválida. Por favor, digite 1 ou 2.")  # Mensagem de erro para escolha inválida

def calculate_lactary(unit_choice):

    #Função que realiza o cálculo do volume diário e por mamada, baseado no peso e idade da criança.
    #O cálculo pode ser realizado em mililitros (ml) ou litros (L), conforme a escolha do usuário.

    print("\n=== Cálculo de Volume para Lactário ===\n")  # Exibe o título do cálculo

    idade = quiz_lac[1][1]  # Acessa a idade da criança
    peso = quiz_lac[2][1]  # Acessa o peso da criança
    mamadas = quiz_lac[6][1]  # Acessa a quantidade de mamadas
    fator_ml_kg = 130 if idade <= 1 else 150  # Define o fator de cálculo com base na idade da criança
    volume_diario = peso * fator_ml_kg  # Calcula o volume diário com base no peso e fator
    volume_por_mamada = volume_diario / mamadas  # Calcula o volume por mamada

    # Ajusta a unidade de medida com base na escolha do usuário
    if unit_choice == "2":
        volume_diario /= 1000  # Converte de ml para L
        volume_por_mamada /= 1000  # Converte de ml para L
        unidade = "L"  # Define unidade como litros

    else:
        unidade = "ml"  # Define unidade como mililitros

    # Exibe o resultado do cálculo
    print("\n=== Resultado do Cálculo ===")
    print(f"Tipo de alimentação: {quiz_lac[4][1]}")
    print(f"Peso: {peso:.2f} kg")  # Exibe o peso da criança
    print(f"Idade: {idade} meses")  # Exibe a idade da criança
    print(f"Volume total por dia: {volume_diario:.2f} {unidade}")  # Exibe o volume total diário
    print(f"Volume por mamada: {volume_por_mamada:.2f} {unidade}")  # Exibe o volume por mamada

    if quiz_lac[7][1].strip():  # Verifica se há observações clínicas
        print(f"Observações clínicas: {quiz_lac[7][1]}")  # Exibe as observações clínicas

    else:
        print("Sem observações clínicas.")  # Caso não haja observações clínicas

    # Armazena os dados modificados
    dados_modificados["nome_da_crianca"] = quiz_lac[0][1]
    dados_modificados["recomendacao"] = f"{quiz_lac[4][1]} / Fórmula: {quiz_lac[5][1]}"
    dados_modificados["volume_prescrito"] = f"{volume_por_mamada:.2f} {unidade} por mamada / {volume_diario:.2f} {unidade} por dia"
    dados_modificados["observacoes"] = quiz_lac[7][1]

def main_lac():

    #Função principal para a realização do questionário e cálculo do lactário.

    quiz()  # Chama a função do questionário
    unit_choice = choose_unit()  # Chama a função para escolher a unidade
    calculate_lactary(unit_choice)  # Chama a função de cálculo

# ---------------------- Visualização e Menu -----------------------

def view_res():

    #Função para visualização dos resultados pelo responsável.
    #Exibe os dados modificados pelo funcionário.

    print("\n=== VISUALIZAÇÃO DO RESPONSÁVEL ===\n")

    if dados_modificados["nome_da_crianca"]:  # Verifica se há dados preenchidos
        print(f"Criança: {dados_modificados['nome_da_crianca']}")  # Exibe o nome da criança
        print(f"Recomendação: {dados_modificados['recomendacao']}")  # Exibe a recomendação
        print(f"Volume prescrito: {dados_modificados['volume_prescrito']}")  # Exibe o volume prescrito

        if dados_modificados["observacoes"]:  # Verifica se há observações clínicas
            print(f"Observações clínicas: {dados_modificados['observacoes']}")  # Exibe as observações clínicas

        else:
            print("Sem observações clínicas.")  # Caso não haja observações clínicas

    else:
        print("Nenhuma recomendação disponível ainda. Aguarde o profissional preencher os dados.")  # Mensagem caso não haja dados

def choose_path(user_permissions):

    # Função para decidir o caminho do usuário, baseado nas permissões.
    # Caso tenha permissão de 'criar' ou 'editar', permite o uso da calculadora.
    # Caso tenha apenas permissão de 'visualizar', mostra os dados preenchidos pelo profissional.

    while True:
        print("\n=== MENU ===")
        if 'criar' in user_permissions or 'editar' in user_permissions:
            print("(1) Preencher questionário e calcular volume")  # opção do funcionário
        if 'visualizar' in user_permissions:
            print("(2) Visualizar recomendações")  # opção do responsável

        print("(3) Logout")  # opção para sair

        opcao = input("Escolha uma opção: ")

        if opcao == "1" and ('criar' in user_permissions or 'editar' in user_permissions):
            main_lac()  # Executa a calculadora

        elif opcao == "2" and 'visualizar' in user_permissions:
            view_res()  # Exibe os dados salvos

        elif opcao == "3":
            logout()  # Faz o logout
            break  # Sai do loop e finaliza o programa

        else:
            print("Opção inválida ou não permitida. Tente novamente.")  # Caso a opção seja inválida

# ---------------------- Execução Principal -----------------------

def main():
    while True:
        permissoes = log_in()  # Realiza o login e retorna as permissões
        choose_path(permissoes)  # Executa o menu baseado nas permissões

        sair = input("Deseja sair do sistema? (s/n): ").strip().lower()
        if sair == "s":
            print("Encerrando o sistema... Até logo!")
            break

# Executa o programa
if __name__ == "__main__":
    main()
