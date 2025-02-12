class tarefa():
    def __init__(self):
        self.titulo = ""
        self.descricao = ""
        self.prioridade = ""
        self.data_ini = ""
        self.hora_ini = ""
        self.data_fim = ""
        self.hora_fim = ""

    def adicionar(self):
        tempdic = {}

        self.titulo = input("Digite o título da tarefa: ")
        self.descricao = input("Digite a descrição da tarefa: ")
        self.prioridade = input("Digite a prioridade da tarefa: ")
        self.data_ini = input("Digite a data de início da tarefa: ")
        self.hora_ini = input("Digite a hora de início da tarefa: ")
        self.data_fim = input("Digite a data de término da tarefa: ")
        self.hora_fim = input("Digite a hora de término da tarefa: ")

        return self
    
    def __str__(self):
        return f"Título: {self.titulo}\nDescrição: {self.descricao}\nPrioridade: {self.prioridade}\nData de início: {self.data_ini}\nHora de início: {self.hora_ini}\nData de término: {self.data_fim}\nHora de término: {self.hora_fim}"