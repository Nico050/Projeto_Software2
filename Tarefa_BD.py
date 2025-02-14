from Tarefa import tarefa
from Contas import conta
from finder_data_task import finder
import pandas as pd
import os

class tarefa_bd():
    def __init__(self):
        self.tarefas_BD = {}

    def adicionar_tarefa(self, useratual, contas):  
        task = tarefa()
        task.adicionar(contas)

        self.tarefas_BD["Titulo"] = task.titulo
        self.tarefas_BD["Descricao"] = task.descricao
        self.tarefas_BD["Prioridade"] = task.prioridade
        self.tarefas_BD["Envolvidos"] = task.envolvidos
        self.tarefas_BD["Data de Inicio"] = task.data_ini
        self.tarefas_BD["Hora de Inicio"] = task.hora_ini
        self.tarefas_BD["Data de Termino"] = task.data_fim
        self.tarefas_BD["Hora de Termino"] = task.hora_fim
        self.tarefas_BD["Username"] = useratual["Username"]

        return self

    def adicionar_aoBD(self, banco):
        tempBD = pd.DataFrame({'Titulo': [self.tarefas_BD["Titulo"]], 'Descricao': [self.tarefas_BD["Descricao"]], 'Prioridade': [self.tarefas_BD["Prioridade"]], 'Envolvidos': [self.tarefas_BD["Envolvidos"]] ,'Data de Inicio': [self.tarefas_BD["Data de Inicio"]], 'Hora de Inicio': [self.tarefas_BD["Hora de Inicio"]], 'Data de Termino': [self.tarefas_BD["Data de Termino"]], 'Hora de Termino': [self.tarefas_BD["Hora de Termino"]], 'Username': [self.tarefas_BD["Username"]]})
        banco = pd.concat([banco, tempBD], ignore_index=True)
        banco.to_csv(f"tasks{self.tarefas_BD["Username"]}.csv", index=False)
        return banco
    
    def adicionarBD_Envolvidos(self):
        if self.tarefas_BD["Envolvidos"] != "":
            for i in self.tarefas_BD["Envolvidos"].split():
                if os.path.exists(f"tasks{i}.csv"):
                    banco = pd.read_csv(f"tasks{i}.csv")
                    tempBD = pd.DataFrame({'Titulo': [self.tarefas_BD["Titulo"]], 'Descricao': [self.tarefas_BD["Descricao"]], 'Prioridade': [self.tarefas_BD["Prioridade"]], 'Envolvidos': [self.tarefas_BD["Envolvidos"]] ,'Data de Inicio': [self.tarefas_BD["Data de Inicio"]], 'Hora de Inicio': [self.tarefas_BD["Hora de Inicio"]], 'Data de Termino': [self.tarefas_BD["Data de Termino"]], 'Hora de Termino': [self.tarefas_BD["Hora de Termino"]], 'Username': [self.tarefas_BD["Username"]]})
                    banco = pd.concat([banco, tempBD], ignore_index=True)
                    banco.to_csv(f"tasks{i}.csv", index=False)

                else:
                    banco = pd.DataFrame(columns=['Titulo', 'Descricao', 'Prioridade', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Username'])
                    tempBD = pd.DataFrame({'Titulo': [self.tarefas_BD["Titulo"]], 'Descricao': [self.tarefas_BD["Descricao"]], 'Prioridade': [self.tarefas_BD["Prioridade"]], 'Envolvidos': [self.tarefas_BD["Envolvidos"]] ,'Data de Inicio': [self.tarefas_BD["Data de Inicio"]], 'Hora de Inicio': [self.tarefas_BD["Hora de Inicio"]], 'Data de Termino': [self.tarefas_BD["Data de Termino"]], 'Hora de Termino': [self.tarefas_BD["Hora de Termino"]], 'Username': [self.tarefas_BD["Username"]]})
                    banco = pd.concat([banco, tempBD], ignore_index=True)
                    banco.to_csv(f"tasks{i}.csv", index=False)

        
                
                