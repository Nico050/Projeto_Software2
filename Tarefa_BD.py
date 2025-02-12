from Tarefa import tarefa
from Contas import conta

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
