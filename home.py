from functions.add import adicionar
from functions.list import listar, listarporcargo, listarativos
from functions.alterarstatus import ativar
from functions.update import alterar
from functions.loadsave import salvar, carregar

funcionarios = carregar()

resp = input("Digite o número da opção desejada: \n1 - Adicionar funcionário\n2 - Listar todos os funcionários\n3 - Listar funcionários por cargo\n4 - Listar funcionários ativos/inativos\n5 - Alterar Status de um funcionário\n6 - Editar dados de um funcionário\n")

if resp == "1":
    funcionarios = adicionar()
    salvar(funcionarios)
elif resp == "2":
    print(listar(funcionarios))
elif resp == "3":
    cargo = input("Digite o cargo para listar os funcionários: ")
    print(listarporcargo(funcionarios, cargo))
elif resp == "4":
    print(listarativos(funcionarios))
elif resp == "5":
    ativar(funcionarios)
    salvar(funcionarios)
elif resp == "6":
    alterar(funcionarios)
    salvar(funcionarios)
else:
    print("Opção inválida")