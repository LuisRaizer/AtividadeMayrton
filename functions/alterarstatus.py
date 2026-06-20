def ativar(funcionarios):
    """Altera (ativa/desativa) o status de um funcionário identificado pelo CPF."""
    ql = input("Insira o CPF do funcionário que você deseja alterar: ").strip()

    for func in funcionarios:
        if ql == str(func.get("CPF")):
            status_atual = "ATIVO" if func.get("Ativo") else "INATIVO"
            print(f"O funcionário {func['Nome']} está atualmente {status_atual}.")
            
            opcao = input("Deseja alterar o status deste funcionário? (S/N): ").strip().upper()
            
            if opcao == 'S':
                func["Ativo"] = not func.get("Ativo")
                novo_status = "ATIVO" if func["Ativo"] else "INATIVO"
                print(f"Status alterado com sucesso para: {novo_status}!")
            else:
                print("Nenhuma alteração foi feita.")
            return
            
    print("Funcionário com o CPF informado não foi encontrado.")