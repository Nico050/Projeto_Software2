from Contas import conta
from Tarefa import tarefa
from Tarefa_BD import tarefa_bd
from Projetos import projeto
import pandas as pd
import os
from finder_data_task import finder
from finder_data_project import finderp

def carregar_contas():
    if os.path.exists("users.csv"):
        pd_contas = pd.read_csv("users.csv")
        contas = pd_contas[['Nome', 'Sobrenome', 'Username', 'Email', 'Senha']].to_dict('records')
    else:
        pd_contas = pd.DataFrame(columns=['Nome', 'Sobrenome', 'Username', 'Email', 'Senha'])
        contas = []
    return pd_contas, contas

tabset = []
tabsetpj = []
pd_contas, contas = carregar_contas()
pd_datatask = pd.DataFrame(columns=['Titulo', 'Descricao', 'Prioridade', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Username'])
pd_datapj = pd.DataFrame(columns=['Titulo', 'Descricao', 'Tarefas', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Envolvidos', 'Manager'])
usuario_atual = {}

def iniciar():
    global contas, useratual, pd_contas, pd_datatask, tabset, pd_datapj, tabsetpj

    pd_contas, contas = carregar_contas()

    print("Bem-vindo ao sistema de gerenciamento de tarefas!")
    opc = input("Caso queira se registrar digite 1\nCaso queira fazer o login digite 2\n")

    if opc == "1":
        acc_reg = conta()
        acc_reg.registrar()

        if acc_reg.username in pd_contas['Username'].values or " " in acc_reg.username:
            print("Usuário já registrado ou inválido!")
            iniciar()

        elif acc_reg.email in pd_contas['Email'].values or "@" not in acc_reg.email:
            print("Email já registrado ou inválido!")
            iniciar()

        pd_contas = acc_reg.registra_BD(pd_contas)
        contas.append(acc_reg.regista_dicio())
        useratual = acc_reg.regista_dicio()
        print("Registrado com sucesso!")
        main()

    elif opc == "2":
        us = input("Digite seu username: ")
        ps = input("Digite sua senha: ")
        login_sucesso = False
        for i in contas:
            if i["Username"] == us and i["Senha"] == ps:
                useratual = i
                print("Logado com sucesso!")
                pd_datatask = finder(us).find_user(us)
                tabset = finder(us).set_tab(pd_datatask)
                pd_datapj = finderp(us).find_user(us)
                tabsetpj = finderp(us).set_tab(pd_datapj)
                login_sucesso = True
                main()

        if not login_sucesso:
            print("Usuário ou senha incorretos!")
            iniciar()

def main():
    opc = input(f"Olá {useratual['Nome']}! O que deseja fazer?\n1 - Adicionar tarefa\n2 - Ver tarefas\n3 - Remover tarefas\n4 - Adicionar projeto\n5 - Ver projetos\n6 - Remover projeto\n7 - Alterar ou Registrar uma conta\n8 - Sair\n")
    if opc == "1":
        global tabset, pd_datatask, contas
        task = tarefa_bd()
        task.adicionar_tarefa(useratual, contas)
        pd_datatask = task.adicionar_aoBD(pd_datatask)
        tabset.append(task.tarefas_BD)
        task.adicionarBD_Envolvidos()
        print("Tarefa adicionada com sucesso!")
        main()

    elif opc == "2":
        print(tabset)
        main()

    elif opc == "3":
        n = input("Digite o título da tarefa que deseja remover: ")
        x = 0

        for i in tabset:
            if n == i["Titulo"] and n in pd_datatask['Titulo'].values and useratual['Username'] == i["Username"]:
                pd_datatask = pd_datatask[pd_datatask['Titulo'] != n]
                pd_datatask.to_csv(f"tasks{useratual['Username']}.csv", index=False)
                tabset.remove(i)
                if i["Envolvidos"] != "":
                    for j in i["Envolvidos"].split():
                        banco = pd.read_csv(f"tasks{j}.csv")
                        banco = banco[banco['Titulo'] != n]
                        banco.to_csv(f"tasks{j}.csv", index=False)
                x = 1
                break

        if x == 0:
            print("Tarefa não encontrada!")
        else:
            print("Tarefa removida com sucesso!")
        main()

    elif opc == "4":
        global tabsetpj, pd_datapj
        pj = projeto(useratual)
        pj.adicionar(contas, useratual)
        pd_datapj = pj.adicionar_aoBD(pd_datapj)
        tabsetpj.append(pj.adicionar_lista())
        print("Projeto adicionado com sucesso!")
        main()

    elif opc == "5":
        print(tabsetpj)
        main()

    elif opc == "6":
        n = input("Digite o título do projeto que deseja remover: ")
        x = 0

        for i in tabsetpj:
            if n == i["Titulo"] and n in pd_datapj['Titulo'].values and useratual['Username'] == i["Manager"]:
                # Remove o projeto do banco de dados do manager
                pd_datapj = pd_datapj[pd_datapj['Titulo'] != n]
                pd_datapj.to_csv(f"projects{useratual['Username']}.csv", index=False)
                tabsetpj.remove(i)

                # Remove as tarefas do projeto do banco de dados dos envolvidos
                for tarefa in i['Tarefas']:
                    print(tarefa)        
                    if tarefa['Envolvidos'] != "":
                        for j in tarefa['Envolvidos'].split():
                            pd_temp = pd.read_csv(f"tasks{j}.csv")
                            pd_temp = pd_temp[pd_temp['Titulo'] != tarefa['Titulo']]
                            pd_temp.to_csv(f"tasks{j}.csv", index = False)

            x = 1
            break

        if x == 0:
            print("Projeto não encontrado!")
        else:
            print("Projeto e tarefas associadas removidos com sucesso!")
        main()

    elif opc == "7":
        iniciar()

    elif opc == "8":
        print("Até mais!")
        exit()

    else:
        print("Opção inválida!")
        main()

iniciar()
