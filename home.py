from functions.add import adicionar
from functions.sample_data import get_sample_funcionarios
from functions.list import listar, listarporcargo, listarativos

funcionarios = get_sample_funcionarios()

resp = input("Digite o número da opção desejada: \n1 - Listar todos os funcionários\n2 - Listar funcionários por cargo\n3 - Listar apenas funcionários ativos\n")

if resp == "1":
    print(listar(funcionarios))
elif resp == "2":
    cargo = input("Digite o cargo para listar os funcionários: ")
    print(listarporcargo(funcionarios, cargo))
elif resp == "3":

    print(listarativos(funcionarios))