from datetime import date

def adicionar():
    nome = input("Digite o nome do funcionário: ")
    dia = int(input("Digite o dia de nascimento do funcionário: "))
    mes = int(input("Digite o mês de nascimento do funcionário: "))
    ano = int(input("Digite o ano de nascimento do funcionário: "))
    data_nascimento = date(ano, mes, dia)
    cpf = int(input("Digite o CPF do funcionário (apenas números): "))
    while len(str(cpf)) != 11:
        print("CPF deve conter exatamente 11 dígitos.")
        cpf = int(input("Digite o CPF do funcionário (apenas números): "))
    cargo = input("Digite o cargo do funcionário: ")
    email = input("Digite o email do funcionário: ")
    telefone = input("Digite o telefone do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    sexo = input("Digite o sexo do funcionário (M/F): ")
    ativo = input("O funcionário está ativo? (S/N): ").strip().upper() == 'S'

    funcionario = {
        "Nome": nome,
        "Data de nascimento": data_nascimento,
        "CPF": cpf,
        "Cargo": cargo,
        "Email": email,
        "Telefone": telefone,
        "Salario": salario,
        "Sexo": sexo,
        "Ativo": ativo,
    }

    return funcionario
