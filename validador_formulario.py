import re

def validar_nome(nome):
    """
    Valida o campo Nome.
    O nome deve ter no máximo 50 símbolos alfabéticos e espaços.
    """
    padrao = re.compile(r"^[a-zA-Z ]{1,50}$")
    if padrao.match(nome):
        return True
    return False

def validar_cpf(cpf):
    """
    Valida o campo CPF.
    O CPF pode conter somente 11 algarismos numéricos ou estar no formato "000.000.000-00".
    """
    padrao = re.compile(r"^(\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})$")
    if padrao.match(cpf):
        return True
    return False

def validar_email(email):
    """
    Valida o campo E-mail.
    - Nome de usuário: mínimo 2 símbolos (alfanuméricos, ponto ou underline).
    - Seguido de '@'.
    - Domínio: mesma regra do nome de usuário.
    - Seguido de '.' e 3 letras minúsculas para o TLD.
    """
    # 1. Nome de usuário: mínimo 2 símbolos (alfanuméricos, ponto ou underline), não pode começar com ponto, nem ter '..'
    usuario_regex = r"(?!\.)(?!.*\.\.)(?!.*\.$)[\w\.]{2,}"
    # 2. Arroba obrigatória
    arroba = r"@"
    # 3. Domínio: mínimo 2 símbolos (alfanuméricos, hífen ou ponto), não pode começar com '.' ou '-', nem ter '..' ou terminar com '.' ou '-'
    dominio_regex = r"(?![.-])(?!.*\.\.)(?!.*[-.]$)[\w\.-]{2,}"
    # 4. TLD: ponto seguido de 3 letras minúsculas
    tld_regex = r"\.[a-z]{3}"
    # 5. Junta tudo
    padrao = re.compile(rf"^{usuario_regex}{arroba}{dominio_regex}{tld_regex}$")
    if padrao.match(email):
        return True
    return False

def validar_telefone(telefone):
    """
    Valida o campo Telefone.
    Dois formatos possíveis: 11 números ou "(00)00000-0000".
    """
    padrao = re.compile(r"^(\d{11}|\(\d{2}\)\d{5}-\d{4})$")
    if padrao.match(telefone):
        return True
    return False

def extrair_emails_validos(texto):
    """
    Extrai todos os e-mails válidos de um texto.
    Utiliza a mesma expressão regular da função de validação de e-mail.
    """
    # Regex ajustada para não capturar e-mails com '..' ou que terminem com '.' antes do TLD.
    padrao_email = re.compile(r"[\w_]+(?:\.[\w_]+)*@[\w-]+(?:\.[\w-]+)*\.[a-z]{3}")
    return padrao_email.findall(texto)

# --- Demonstração ---
if __name__ == "__main__":
    print("--- Validador de Formulário ---")

    # Exemplos de dados para validação
    dados_formulario = {
        "Nome": "Joao da Silva",
        "CPF": "123.456.789-00",
        "E-mail": "joao.silva@meu-dominio.com",
        "Telefone": "(11)98765-4321"
    }

    print("\nValidando os seguintes dados:")
    for campo, valor in dados_formulario.items():
        print(f"- {campo}: {valor}")

    print("\nResultados da Validação:")
    print(f"Nome válido: {validar_nome(dados_formulario['Nome'])}")
    print(f"CPF válido: {validar_cpf(dados_formulario['CPF'])}")
    print(f"E-mail válido: {validar_email(dados_formulario['E-mail'])}")
    print(f"Telefone válido: {validar_telefone(dados_formulario['Telefone'])}")

    # Testando com dados inválidos
    print("\nTestando com dados inválidos:")
    print(f"Nome inválido ('Nome com 123'): {validar_nome('Nome com 123')}")
    print(f"CPF inválido ('123.456.789'): {validar_cpf('123.456.789')}")
    print(f"E-mail inválido ('email@dominio..com'): {validar_email('email@dominio..com')}")
    print(f"Telefone inválido ('99887766'): {validar_telefone('99887766')}")


    print("\n--- Extração de E-mails ---")

    texto_para_extracao = """
    Prezado usuário,

    Aqui estão os contatos do nosso time de suporte:

    - alice.souza@gmail.com

    - suporte_23@empresa-tech.com

    - joao99@dominio123.org

    - erro.email@gmail..com

    Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.

    Atenciosamente,

    Equipe de Atendimento
    """

    emails_encontrados = extrair_emails_validos(texto_para_extracao)

    print("\nTexto analisado:")
    print(texto_para_extracao)
    print("\nE-mails válidos extraídos do texto:")
    if emails_encontrados:
        for email in emails_encontrados:
            print(f"- {email}")
    else:
        print("Nenhum e-mail válido encontrado.")
