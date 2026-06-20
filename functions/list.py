def listar(funcionarios):
    funcionarios_list = []
    for func in funcionarios:
        nome = func["Nome"]
        funcionarios_list.append(nome)
    return funcionarios_list

def listarporcargo(funcionarios, cargo):
    print(f"Listando funcionários pelo cargo de {cargo}: ")
    funcionarios_encontrados = []
    for func in funcionarios:
        if func["Cargo"] == cargo:
            funcionarios_encontrados.append(func["Nome"])
    return funcionarios_encontrados

def listarativos(funcionarios):
    resp = input("Deseja listar apenas os funcionários ativos? (S/N): ").strip().upper()
    if resp != 'S':
        print("Listando funcionários inativos: ")
        funcionarios_inativos = []
        for func in funcionarios:
            if not func["Ativo"]:
                funcionarios_inativos.append(func["Nome"])
        return funcionarios_inativos
    else:
        print("Listando funcionários ativos: ")
        funcionarios_ativos = []
        for func in funcionarios:
            if func["Ativo"]:
                funcionarios_ativos.append(func["Nome"])
        return funcionarios_ativos
