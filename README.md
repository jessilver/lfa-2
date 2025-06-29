# lfa-2

# Validador de Formulário e Extração de E-mails

Este projeto implementa uma aplicação em Python para validar o preenchimento de um formulário e extrair e-mails válidos de um texto, utilizando expressões regulares (`import re`).

## Funcionalidades

- **Validação de Formulário**:
  - **Nome**: até 50 caracteres, aceita letras (com acento) e espaço.
  - **CPF**: aceita 11 dígitos ou formato `000.000.000-00`.
  - **E-mail**: usuário com pelo menos 2 caracteres alfanuméricos, ponto ou underline, seguido de `@`, domínio com a mesma regra, terminando com ponto e 3 letras minúsculas.
  - **Telefone**: aceita 11 dígitos ou formato `(00)00000-0000`.

- **Extração de E-mails**:
  - Varre um texto e retorna apenas e-mails válidos conforme a expressão regular definida.

## Como usar

1. Execute o projeto com:
   ```bash
   python3 main.py
   ```
2. Escolha a opção desejada no menu:
   - Validar dados de formulário
   - Extrair e-mails válidos de um texto

## Exemplo de texto para extração

```
Prezado usuário,

Aqui estão os contatos do nosso time de suporte:

- alice.souza@gmail.com
- suporte_23@empresa-tech.com
- joao99@dominio123.org
- erro.email@gmail..com

Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.

Atenciosamente,
Equipe de Atendimento
```

Apenas os e-mails válidos serão extraídos.
