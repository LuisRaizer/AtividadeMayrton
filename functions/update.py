def alterar(funcionarios):
    pf = input("Insira o CPF do funcionário que você deseja alterar: ").strip()

    for func in funcionarios:
        if pf == str(func["cpf"]):
            opcao = int(input("Qual informação você deseja alterar?\n1 - Nome\n2 - Data de Nascimento\n3 - CPF\n4 - Cargo\n5 - Email\n6 - Telefone\n7 - Salário\n8 - Sexo\nOpção: "))
            
            if opcao == 1:
                nv = input("Insira o novo nome completo do funcionário: ").strip()
                func["nome"] = nv
                print("Nome alterado com sucesso!")
            elif opcao == 2:
                nv = input("Insira a nova data de nascimento (DD/MM/AAAA): ").strip()
                func["data_nascimento"] = nv
                print("Data de nascimento alterada com sucesso!")
            elif opcao == 3:
                nv = input("Insira o novo CPF do funcionário: ").strip()
                func["cpf"] = nv
                print("CPF alterado com sucesso!")
            elif opcao == 4:
                nv = input("Insira o novo cargo do funcionário: ").strip()
                func["cargo"] = nv
                print("Cargo alterado com sucesso!")
            elif opcao == 5:
                nv = input("Insira o novo e-mail do funcionário: ").strip()
                func["email"] = nv
                print("E-mail alterado com sucesso!")
            elif opcao == 6:
                nv = input("Insira o novo telefone do funcionário: ").strip()
                func["telefone"] = nv
                print("Telefone alterado com sucesso!")
            elif opcao == 7:
                nv = float(input("Insira o novo salário do funcionário: "))
                func["salario"] = nv
                print("Salário alterado com sucesso!")
            elif opcao == 8:
                nv = input("Insira o sexo do funcionário: ").strip()
                func["sexo"] = nv
                print("Sexo alterado com sucesso!")
            else:
                print("Opção inválida.")
                
            return
            
    print("Funcionário com o CPF informado não foi encontrado.")