import pandas as pd
import os

class finder():
    def __init__(self, user):
        self.user = user

    def find_user(self, user):
        if os.path.exists(f"tasks{self.user}.csv"):
            pd_tarefas = pd.read_csv(f"tasks{self.user}.csv")
            return pd_tarefas
        else:
            pd_tarefas = pd.DataFrame(columns=['Titulo', 'Descricao', 'Prioridade', 'Envolvidos' ,'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Username'])
            pd_tarefas.to_csv(f"tasks{self.user}.csv", index=False)
            return pd_tarefas
        
    def set_tab(self, pd_tarefas):
        if os.path.exists(f"tasks{self.user}.csv"):
            tabset = pd_tarefas[['Titulo', 'Descricao', 'Prioridade', 'Envolvidos', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Username']].to_dict('records')
        else:
            tabset = []
        return tabset