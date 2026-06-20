def alterar(funcionarios):
    cpf = int(input("Insira o CPF do funcionário que você deseja alterar: ").strip())

    for func in funcionarios:
        if cpf == func.get("CPF"):
            opcao = int(input("Qual informação você deseja alterar?\n1 - Nome\n2 - Data de Nascimento\n3 - CPF\n4 - Cargo\n5 - Email\n6 - Telefone\n7 - Salário\n8 - Sexo\nOpção: "))
            
            if opcao == 1:
                nv = input("Insira o novo nome completo do funcionário: ").strip()
                func["Nome"] = nv
                print("Nome alterado com sucesso!")
                print(func)
            elif opcao == 2:
                nv = input("Insira a nova data de nascimento (DD/MM/AAAA): ").strip()
                func["Data de nascimento"] = nv
                print("Data de nascimento alterada com sucesso!")
            elif opcao == 3:
                nv = int(input("Insira o novo CPF do funcionário: ").strip())
                func["CPF"] = nv
                print("CPF alterado com sucesso!")
            elif opcao == 4:
                nv = input("Insira o novo cargo do funcionário: ").strip()
                func["Cargo"] = nv
                print("Cargo alterado com sucesso!")
            elif opcao == 5:
                nv = input("Insira o novo e-mail do funcionário: ").strip()
                func["Email"] = nv
                print("E-mail alterado com sucesso!")
            elif opcao == 6:
                nv = input("Insira o novo telefone do funcionário: ").strip()
                func["Telefone"] = nv
                print("Telefone alterado com sucesso!")
            elif opcao == 7:
                nv = float(input("Insira o novo salário do funcionário: "))
                func["Salario"] = nv
                print("Salário alterado com sucesso!")
            elif opcao == 8:
                nv = input("Insira o sexo do funcionário: ").strip()
                func["Sexo"] = nv
                print("Sexo alterado com sucesso!")
            else:
                print("Opção inválida.")
                
            return
            
    print("Funcionário com o CPF informado não foi encontrado.")