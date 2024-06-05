class Certificado:
    def __init__(self, id, descricao, data_expiracao, id_funcionario=None):
        self.id = id
        self.descricao = descricao
        self.data_expiracao = data_expiracao
        self.id_funcionario = id_funcionario

    def __repr__(self):
        return f"<Certificado {self.descricao}, Expira em: {self.data_expiracao}>"