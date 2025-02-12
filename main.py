from Contas import conta
from Tarefa import tarefa
from Tarefa_BD import tarefa_bd


usuario_atual = {}
contas = []
tabset = []

def iniciar():
    global contas, useratual
    print("Bem-vindo ao sistema de gerenciamento de tarefas!")
    opc = input("Caso para se registrar digite 1\nCaso para fazer login digite 2\n")
    if opc == "1":
        acc_reg = conta()
        acc_reg.registrar()
        contas.append(acc_reg.regista_dicio())
        useratual = acc_reg.regista_dicio()
        print("Registrado com sucesso!")
        main()

    elif opc == "2":
        u = input("Digite seu username: ")
        p = input("Digite sua senha: ")
        for u in contas:
            if u["Username"] == u and u["Senha"] == p:
                useratual = u 
                print("Logado com sucesso!")
                main()
            else:
                print("Username ou senha incorretos!")
                iniciar()

def main():
    opc = input(f"Olá {useratual['Nome']}! O que deseja fazer?\n1 - Adicionar tarefa\n2 - Ver tarefas\n3 - Remover tarefas\n4 - Alterar ou Registrar uma conta\n5 - Sair\n")
    if opc == "1":
        global tabset
        task = tarefa_bd()
        task.adicionar_tarefa(useratual)
        tabset.append(task.tarefas_BD)
        print("Tarefa adicionada com sucesso!")
        main()

    elif opc == "2":
        print(tabset)
        main()

    elif opc == "3":
        n = input("Digite o título da tarefa que deseja remover: ")

        for i in tabset:
            if n == i["Titulo"]:
                tabset.remove(i)
                print("Tarefa removida com sucesso!")
                break
            else:
                print("Tarefa não encontrada!")

        main()

    elif opc == "4":
        iniciar()

    elif opc == "5":

        pass
    else:
        print("Opção inválida!")
        main()

    

iniciar()

