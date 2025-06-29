from validador_formulario import validar_nome, validar_cpf, validar_email, validar_telefone, extrair_emails_validos

def menu():
    print("\n--- Validador de Formulário (Interface) ---")
    print("1. Validar dados de formulário")
    print("2. Extrair e-mails válidos de um texto")
    print("0. Sair")
    return input("Escolha uma opção: ")

def validar_formulario():
    print("\nPreencha os dados do formulário:")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    print("\nResultados da Validação:")
    print(f"Nome válido: {validar_nome(nome)}")
    print(f"CPF válido: {validar_cpf(cpf)}")
    print(f"E-mail válido: {validar_email(email)}")
    print(f"Telefone válido: {validar_telefone(telefone)}")

def extrair_emails():
    print("\nDigite o texto para extração de e-mails (finalize com uma linha vazia):")
    linhas = []
    while True:
        linha = input()
        if linha.strip() == "":
            break
        linhas.append(linha)
    texto = "\n".join(linhas)
    emails = extrair_emails_validos(texto)
    print("\nE-mails válidos extraídos:")
    if emails:
        for email in emails:
            print(f"- {email}")
    else:
        print("Nenhum e-mail válido encontrado.")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            validar_formulario()
        elif opcao == "2":
            extrair_emails()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
