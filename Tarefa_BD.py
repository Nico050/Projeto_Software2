from Tarefa import tarefa
from Contas import conta
import pandas as pd

class tarefa_bd():
    def __init__(self):
        self.tarefas_BD = {}

    def adicionar_tarefa(self, useratual):
        task = tarefa()
        task.adicionar()

        self.tarefas_BD["Titulo"] = task.titulo
        self.tarefas_BD["Descricao"] = task.descricao
        self.tarefas_BD["Prioridade"] = task.prioridade
        self.tarefas_BD["Data de Inicio"] = task.data_ini
        self.tarefas_BD["Hora de Inicio"] = task.hora_ini
        self.tarefas_BD["Data de Termino"] = task.data_fim
        self.tarefas_BD["Hora de Termino"] = task.hora_fim
        self.tarefas_BD["Username"] = useratual["Username"]

        return self

    def adicionar_aoBD(self, banco):
        tempBD = pd.DataFrame({'Titulo': [self.tarefas_BD["Titulo"]], 'Descricao': [self.tarefas_BD["Descricao"]], 'Prioridade': [self.tarefas_BD["Prioridade"]], 'Data de Inicio': [self.tarefas_BD["Data de Inicio"]], 'Hora de Inicio': [self.tarefas_BD["Hora de Inicio"]], 'Data de Termino': [self.tarefas_BD["Data de Termino"]], 'Hora de Termino': [self.tarefas_BD["Hora de Termino"]], 'Username': [self.tarefas_BD["Username"]]})
        banco = pd.concat([banco, tempBD], ignore_index=True)
        banco.to_csv(f"tasks{self.tarefas_BD["Username"]}.csv", index=False)
        return banco