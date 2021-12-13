from furadeira import Furadeira
from lixadeira import Lixadeira

furadeiras = {}
lixadeiras = {}

menu = 1

while menu > 0:
    print("Ferragem do seu Zé")
    print("========= Menu ========")
    print("0 - Sair")
    print("1 - Cadastrar Furadeira")
    print("2 - Cadastrar Lixadeira")
    print("3 - Mostrar informações")
    
    menu = int(input("Informe uma ação: "))

    if menu == 1:
        furadeira_obj = Furadeira.cadastrar()
        furadeira_obj.getInformacoes()
        furadeiras[furadeira_obj.nome] = {}
        furadeiras[furadeira_obj.nome]["Objeto"] = furadeira_obj

    if menu == 2:
        lixadeira_obj = Lixadeira.cadastrar()
        lixadeira_obj.getInformacoes()
        lixadeiras[lixadeira_obj.nome]["Objeto"] = lixadeira_obj


    if menu == 3:
        print("1 - Para Furadeiras")
        print("2 - Para Lixadeiras")
        escolha = int(input("Qual feramenta você deseja? "))
        if escolha == 1:
            nome = input('Infome o nome: ')
            try:
                furadeiras[nome]["Objeto"].getInformacoes()
            except:
                print(f"Não foi encontrado nenhuma furadeira com esse nome: {nome}")
        if escolha == 2:
            nome = input('Infome o nome: ')
            try:
                lixadeiras[nome]["Objeto"].getInformacoes()
            except:
                print(f"Não foi encontrado nenhuma lixadeira com esse nome: {nome}")

