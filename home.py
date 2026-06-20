from functions.add import adicionar
from functions.list import listar, listarporcargo, listarativos
from functions.alterarstatus import ativar
from functions.update import alterar

funcionarios = get_sample_funcionarios()

resp = input("Digite o número da opção desejada: \n1 - Listar todos os funcionários\n2 - Listar funcionários por cargo\n3 - Listar apenas funcionários ativos\n4 - Alterar Status de um funcionário\n5 - Editar dados de um funcionário")

if resp == "1":
    print(listar(funcionarios))
elif resp == "2":
    cargo = input("Digite o cargo para listar os funcionários: ")
    print(listarporcargo(funcionarios, cargo))
elif resp == "3":
    print(listarativos(funcionarios))
elif resp == "4":
    ativar(funcionarios)
elif resp == "5":
    alterar(funcionarios)