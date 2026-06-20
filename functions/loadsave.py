def salvar(funcionarios, nome_arquivo="funcionarios.txt"):
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    
    for func in funcionarios:
        linha = f"{func['CPF']};{func['Nome']};{func['Data de nascimento']};{func['Cargo']};{func['Email']};{func['Telefone']};{func['Salario']};{func['Sexo']};{func['Ativo']}\n"
        arquivo.write(linha)
        
    arquivo.close()
    print("Dados salvos com sucesso no arquivo TXT!")