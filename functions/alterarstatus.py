def ativar(funcionarios):
    ql = input("Insira o CPF do funcionário que você deseja alterar: ").strip()

    for func in funcionarios:
        if ql == str(func["cpf"]):
            status_atual = "ATIVO" if func["ativo"] else "INATIVO"
            print(f"O funcionário {func['nome']} está atualmente {status_atual}.")
            
            opcao = input("Deseja alterar o status deste funcionário? (S/N): ").strip().upper()
            
            if opcao == 'S':
                func["ativo"] = not func["ativo"]
                novo_status = "ATIVO" if func["ativo"] else "INATIVO"
                print(f"Status alterado com sucesso para: {novo_status}!")
            else:
                print("Nenhuma alteração foi feita.")
            return
            
    print("Funcionário com o CPF informado não foi encontrado.")