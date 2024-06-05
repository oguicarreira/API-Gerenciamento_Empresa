class Funcionario:
    def __init__(self, id, nome, cpf, data_nasc, cidade, estado, endereco, celular=None, categoria_cnh=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.cidade = cidade
        self.estado = estado
        self.endereco = endereco
        self.celular = celular
        self.categoria_cnh = categoria_cnh

    def __repr__(self):
        return f"<Funcionario {self.nome}, {self.cpf}>"