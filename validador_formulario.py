import re

def validar_nome(nome):
    """
    Valida o campo Nome.
    - Apenas letras maiúsculas/minúsculas e espaço
    - Entre 1 e 50 caracteres
    """
    padrao = re.compile(
        r"^[a-zA-Z ]{1,50}$"  # Letras e espaço, de 1 a 50 caracteres
    )
    return bool(padrao.fullmatch(nome))

def validar_cpf(cpf):
    """
    Valida o campo CPF.
    - 11 dígitos numéricos OU
    - Formato 000.000.000-00 (com pontos nas posições 3 e 7 e hífen na posição 11)
    """
    padrao = re.compile(
        r"^(\d{11}"  # 11 dígitos numéricos
        r"|\d{3}\.\d{3}\.\d{3}-\d{2})$"  # ou formato com pontos e hífen
    )
    return bool(padrao.fullmatch(cpf))

def validar_email(email):
    """
    Valida o campo E-mail.
    - Usuário: mínimo 2 símbolos alfanuméricos, ponto ou underline
    - Não pode começar ou terminar com ponto, nem ter '..'
    - Seguido de '@'.
    - Domínio: mesma regra do usuário, mínimo 2 símbolos, não pode começar/terminar com ponto ou hífen, nem ter '..'
    - TLD: ponto seguido de 3 letras minúsculas (obrigatório, exatamente 3)
    """
    padrao = re.compile(
        r"^(?!\.)"              # Não pode começar com ponto
        r"(?!.*\.\.)"          # Não pode ter dois pontos consecutivos
        r"[\w._]{2,}"          # Usuário
        r"(?<!\.)"             # Não pode terminar com ponto
        r"@"
        r"(?![.-])"             # Domínio não pode começar com ponto ou hífen
        r"[\w._-]{2,}"         # Domínio
        r"(?<![.-])"            # Domínio não pode terminar com ponto ou hífen
        r"\.[a-z]{3}$"         # TLD
    )
    return bool(padrao.match(email))

def validar_telefone(telefone):
    """
    Valida o campo Telefone.
    - 11 dígitos numéricos OU
    - Formato (00)00000-0000
    """
    padrao = re.compile(
        r"^(\d{11}"  # 11 dígitos numéricos
        r"|\(\d{2}\)\d{5}-\d{4})$"  # ou formato (00)00000-0000
    )
    return bool(padrao.match(telefone))

def extrair_emails_validos(texto):
    """
    Extrai todos os e-mails válidos de um texto.
    Utiliza a função de validação de e-mail para filtrar apenas os válidos.
    """
    candidatos = re.findall(r"[\w._-]+@[\w.-]+\.[a-z]{3}", texto)
    return [email for email in candidatos if validar_email(email)]

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
