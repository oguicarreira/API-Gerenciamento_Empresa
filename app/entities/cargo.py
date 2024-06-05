class Cargo:
    def __init__(self, id, descricao, id_funcionario=None):
        self.id = id
        self.descricao = descricao
        self.id_funcionario = id_funcionario

    def __repr__(self):
        return f"<Cargo {self.descricao}, Funcionario ID: {self.id_funcionario}>"