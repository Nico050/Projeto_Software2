
class conta():
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.username = ""
        self.email = ""
        self.password = ""

    def registrar(self):
        print("Registre-se")
        self.nome = input("Digite seu nome: ")
        self.sobrenome = input("Digite seu sobrenome: ")
        self.username = input("Digite seu username: ")
        self.email = input("Digite seu email: ")
        self.password = input("Digite sua senha: ")

        return self

    def regista_dicio(self):
        dicio = {}
        dicio["Nome"] = self.nome
        dicio["Sobrenome"] = self.sobrenome
        dicio["Username"] = self.username
        dicio["Email"] = self.email
        dicio["Senha"] = self.password

        return dicio



    def __str__(self):
        return f"Nome: {self.nome}\nSobrenome: {self.sobrenome}\nUsername: {self.username}\nEmail: {self.email}\nSenha: {self.password}"