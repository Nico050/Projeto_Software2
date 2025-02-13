from Contas import conta
from Tarefa import tarefa
from Tarefa_BD import tarefa_bd
import pandas as pd
import os
from finder_data_task import finder

if os.path.exists("users.csv"):
    pd_contas = pd.read_csv("users.csv")
    contas = pd_contas[['Nome', 'Sobrenome', 'Username', 'Email', 'Senha']].to_dict('records')
else:
    pd_contas = pd.DataFrame(columns=['Nome', 'Sobrenome', 'Username', 'Email', 'Senha'])
    contas = []

pd_datatask = pd.DataFrame(columns=['Titulo', 'Descricao', 'Prioridade', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Username'])

usuario_atual = {}

def iniciar():
    global contas, useratual, pd_contas, pd_datatask, tabset
    print("Bem-vindo ao sistema de gerenciamento de tarefas!")
    print(contas)
    opc = input("Caso queira se registrar digite 1\nCaso queira fazer o login digite 2\n")
    if opc == "1":
        acc_reg = conta()
        acc_reg.registrar()

        if acc_reg.username in pd_contas['Username'].values:
            print("Usuário já registrado!")
            iniciar()

        elif acc_reg.email in pd_contas['Email'].values or "@" not in acc_reg.email:
            print("Email já registrado! / Email inválido!")
            iniciar()

        pd_contas = acc_reg.registra_BD(pd_contas)
        contas.append(acc_reg.regista_dicio())
        useratual = acc_reg.regista_dicio()
        print("Registrado com sucesso!")
        main()

    elif opc == "2":
        us = input("Digite seu username: ")
        ps = input("Digite sua senha: ")
        for i in contas:
            print(i)
            print(i["Username"])
            print(i["Senha"])
            if i["Username"] == us and i["Senha"] == ps:
                useratual = i
                print("Logado com sucesso!")
                pd_datatask = finder(us).find_user(us)
                tabset = finder(us).set_tab(pd_datatask)
                main()
        print("Usuário ou senha incorretos!")
        iniciar()

def main():
    opc = input(f"Olá {useratual['Nome']}! O que deseja fazer?\n1 - Adicionar tarefa\n2 - Ver tarefas\n3 - Remover tarefas\n4 - Alterar ou Registrar uma conta\n5 - Sair\n")
    if opc == "1":
        global tabset, pd_datatask
        task = tarefa_bd()
        task.adicionar_tarefa(useratual)
        pd_datatask = task.adicionar_aoBD(pd_datatask)
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
        print("Até mais!")
        exit()
    else:
        print("Opção inválida!")
        main()

iniciar()