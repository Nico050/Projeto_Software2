from Tarefa import tarefa
from Tarefa_BD import tarefa_bd
import pandas as pd

class projeto():
    def __init__(self, usuario):
        self.titulo = ""
        self.descricao = ""
        self.tarefas = []
        self.data_ini = ""
        self.hora_ini = ""
        self.data_fim = ""
        self.hora_fim = ""
        self.envolvidos = ""
        self.manager = usuario["Username"]

    def adicionar(self, contas, useratual):
        self.titulo = input("Digite o título do projeto: ")
        self.descricao = input("Digite a descrição do projeto: ")
        self.tarefas = []
        qtd = 0
        while True:
            qtd = int(input("Quantas tarefas o projeto terá? "))
            if qtd == 0:
                print("Projeto sem tarefas não é projeto!")
            else:
                break
        for i in range(qtd):
            task = tarefa_bd()
            task.adicionar_tarefa(useratual, contas)
            self.tarefas.append(task.tarefas_BD)
            task.adicionarBD_Envolvidos()

        self.data_ini = input("Digite a data de início do projeto: ")
        self.hora_ini = input("Digite a hora de início do projeto: ")
        self.data_fim = input("Digite a data de término do projeto: ")
        self.hora_fim = input("Digite a hora de término do projeto: ")
        
        for i in self.tarefas:

            for j in i["Envolvidos"].split():
                if j not in self.envolvidos:
                    self.envolvidos += j + " "

        return self
    
    def adicionar_lista(self):
        tempdic = {}
        tempdic["Titulo"] = self.titulo
        tempdic["Descricao"] = self.descricao
        tempdic["Tarefas"] = self.tarefas
        tempdic["Data de Inicio"] = self.data_ini
        tempdic["Hora de Inicio"] = self.hora_ini
        tempdic["Data de Termino"] = self.data_fim
        tempdic["Hora de Termino"] = self.hora_fim
        tempdic["Envolvidos"] = self.envolvidos
        tempdic["Manager"] = self.manager

        return tempdic
    
    def adicionar_aoBD(self, banco,):
        tempBD = pd.DataFrame({'Titulo': [self.titulo], 'Descricao': [self.descricao], 'Tarefas': [self.tarefas], 'Data de Inicio': [self.data_ini], 'Hora de Inicio': [self.hora_ini], 'Data de Termino': [self.data_fim], 'Hora de Termino': [self.hora_fim], 'Envolvidos': [self.envolvidos], 'Manager': [self.manager]})
        banco = pd.concat([banco, tempBD], ignore_index=True)
        banco.to_csv(f"projects{self.manager}.csv", index=False)
        return banco
        