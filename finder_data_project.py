import pandas as pd
import os

class finderp():
    def __init__(self, user):
        self.user = user

    def find_user(self, user):
        if os.path.exists(f"projects{self.user}.csv"):
            pd_projetos = pd.read_csv(f"projects{self.user}.csv")
            return pd_projetos
        else:
            pd_projetos = pd.DataFrame(columns=['Titulo', 'Descricao', 'Tarefas', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Envolvidos', 'Manager'])
            pd_projetos.to_csv(f"projects{self.user}.csv", index=False)
            return pd_projetos
        
    def set_tab(self, pd_projetos):
        if os.path.exists(f"projects{self.user}.csv"):
            tabset = pd_projetos[['Titulo', 'Descricao', 'Tarefas', 'Data de Inicio', 'Hora de Inicio', 'Data de Termino', 'Hora de Termino', 'Envolvidos', 'Manager']].to_dict('records')
        else:
            tabset = []
        return tabset