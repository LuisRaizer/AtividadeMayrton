def salvar(funcionarios, nome_arquivo="funcionarios.txt"):
    """Salva a lista de funcionários em um arquivo texto."""
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    
    for func in funcionarios:
        linha = f"{func['CPF']};{func['Nome']};{func['Data de nascimento']};{func['Cargo']};{func['Email']};{func['Telefone']};{func['Salario']};{func['Sexo']};{func['Ativo']}\n"
        arquivo.write(linha)
        
    arquivo.close()
    print("Dados salvos com sucesso")

def carregar(nome_arquivo="funcionarios.txt"):
    """Carrega e retorna a lista de funcionários do arquivo, se existir."""
    funcionarios = []
    
    try:
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        
        for linha in arquivo:
            cpf, nome, data_nascimento, cargo, email, telefone, salario, sexo, ativo = linha.strip().split(";")
            funcionario = {
                "CPF": int(cpf),
                "Nome": nome,
                "Data de nascimento": data_nascimento,
                "Cargo": cargo,
                "Email": email,
                "Telefone": telefone,
                "Salario": float(salario),
                "Sexo": sexo,
                "Ativo": ativo == "True"
            }
            funcionarios.append(funcionario)
        
        arquivo.close()
        print("Dados carregados")
    except FileNotFoundError:
        print("Arquivo não encontrado. Nenhum dado foi carregado.")
    
    return funcionarios