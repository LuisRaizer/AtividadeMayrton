from datetime import date

def get_sample_funcionarios():
# para testes
    funcionarios = [
        {
            "Nome": "Maria Silva",
            "Data de nascimento": date(1990, 5, 14),
            "CPF": 12345678901,
            "Cargo": "Desenvolvedor",
            "Email": "maria.silva@example.com",
            "Telefone": "(11) 99999-0001",
            "Salario": 4500.00,
            "Sexo": "F",
            "Ativo": True,
        },
        {
            "Nome": "João Pereira",
            "Data de nascimento": date(1985, 11, 3),
            "CPF": 23456789012,
            "Cargo": "Desenvolvedor",
            "Email": "joao.pereira@example.com",
            "Telefone": "(21) 98888-0002",
            "Salario": 6000.00,
            "Sexo": "M",
            "Ativo": True,
        },
        {
            "Nome": "Ana Costa",
            "Data de nascimento": date(1998, 2, 27),
            "CPF": 34567890123,
            "Cargo": "Estagiário",
            "Email": "ana.costa@example.com",
            "Telefone": "(31) 97777-0003",
            "Salario": 1500.00,
            "Sexo": "F",
            "Ativo": False,
        },
    ]
    return funcionarios
